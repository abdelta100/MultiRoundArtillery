from PowderCharge import PowderCharge


class ArtyRound:
    def __init__(self, caliber: float, weight: float, powderWeight: float, powderenergy):
        self.caliber = caliber
        self.weight = weight
        self.baseCharge = PowderCharge(powderWeight, powderenergy)
        pass

    def prep(self):
        #TODO involve barrel lenght in acceleration
        pass

    def fire(self):
        print("round Fired")
        pass

    def addCharge(self, additionalCharge: float, additionalChargeEnergy:float):
        self.baseCharge.addAdditionalPowder(additionalCharge, additionalChargeEnergy)

    @staticmethod
    def newRoundFromBase(round):
        if isinstance(round, ArtyRound):
            return ArtyRound(round.caliber, round.weight, round.baseCharge.powder, round.baseCharge.energyconstant)

        else:
            raise Exception
            print ("Wrong Base Round")
