from ArtyRound import ArtyRound
from Barrel import Barrel
from GlobalCoordinates import Global
import threading


class ArtilleryGun:
    def __init__(self):
        self.pos = Global(0, 0, 0)
        self.azimuth = 0
        self.barrel = Barrel(20, 0.125, 20)
        self.baseRound = ArtyRound(self.barrel.diameter, 10, 20, 30)
        self.additionalPowderEnergy = 30
        self.programmedRounds: list[dict] = []
        self.rotationVelocity = 20  # degrees/second?
        self.simCurrentTime=0
        self.solutionAcquired = False
        self.acquiringSolution=False
        self.tick=1/60

    def firingSolution(self, target, num_rounds):
        # return array of angle and additional powder charge and time at fire for each round
        sol = [{"angle": 30, "powder": 40, "time": 1},
               {"angle": 50, "powder": 45, "time": 5}]

        self.programmedRounds = sol
        self.solutionAcquired=True

    def firingBarrage(self, target, num_rounds):

        if not self.solutionAcquired and not self.acquiringSolution:
            calculatingSolution = threading.Thread(self.firingSolution(target, num_rounds))
            calculatingSolution.start()
            self.acquiringSolution = True
        #TODO add multithreading for sim and solution calculation?
        for roundparams in self.programmedRounds:
            round = ArtyRound.newRoundFromBase(self.baseRound)
            round.addCharge(roundparams["powder"], self.additionalPowderEnergy)
            if self.simCurrentTime>=roundparams["time"] and self.azimuth == roundparams['angle']:
                round.fire()
                self.programmedRounds.remove(roundparams)

        self.step(self.tick)

    def fire(self, round: ArtyRound):
        round.prep()
        round.fire()
        pass

    def step(self, timestep):
        self.simCurrentTime+=timestep
        self.azimuthSeek()

    def azimuthSeek(self):
        if len(self.programmedRounds)>0:
            self.vertRotateBarrel(self.programmedRounds[0]['angle'])
        print(self.azimuth)

    def vertRotateBarrel(self, angle):
        #TODO make this more elegant
        move_angle = angle-self.azimuth
        try:
            move_dir=move_angle/abs(move_angle)
        except ZeroDivisionError:
            move_dir=0
        self.azimuth += min(move_angle,move_dir*self.rotationVelocity * self.tick)
        self.barrel.angle = self.azimuth

