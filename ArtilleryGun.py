from ArtyRound import ArtyRound
from Barrel import Barrel
from GlobalCoordinates import Global


class ArtilleryGun:
    def __init__(self):
        self.pos = Global(0, 0, 0)
        self.angle = 0
        self.barrel = Barrel(20, 0.125, 20)
        self.baseRound = ArtyRound(self.barrel.diameter, 10, 20)
        self.programmedRounds: list[dict] = []
        self.rotationVelocity = 20  # degrees/second?

    def firingSolution(self, target, num_rounds):
        # return array of angle and additional powder charge and time at fire for each round
        sol = [{"angle": 30, "powder": 40, "time": 1},
               {"angle": 50, "powder": 45, "time": 5}]

        self.programmedRounds = sol

        return sol

    def firingSim(self):
        for roundparams in self.programmedRounds:
            round = ArtyRound.newRoundFromBase(self.baseRound)
            round.addCharge(roundparams["powder"])

    def fire(self, round: ArtyRound):
        round.prep()
        round.fire()
        pass
