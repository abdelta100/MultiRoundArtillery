class PowderCharge:

    def __init__(self, powderWeight: float, energy):
        self.powder = powderWeight
        self.energyconstant = energy
        pass

    def addAdditionalPowder(self, additionalCharge, additionalChargeEnergy):
        self.powder += additionalCharge*(additionalChargeEnergy/self.energyconstant)

    @property
    def energy(self):
        return self.powder*self.energyconstant