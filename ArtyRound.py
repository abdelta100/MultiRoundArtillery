from PowderCharge import PowderCharge


class ArtyRound:
    def __init__(self, caliber: float, weight: float, powderWeight: float):
        self.caliber = caliber
        self.weight = weight
        self.baseCharge = PowderCharge(powderWeight)
        pass

    def prep(self):
        pass

    def fire(self):
        pass

    @staticmethod
    def newRoundFromBase(round):
        if isinstance(round, ArtyRound):
            return ArtyRound(round.caliber, round.weight, round.baseCharge)

        else:
            raise Exception
            print ("Wrong Base Round")
