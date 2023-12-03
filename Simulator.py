from ArtilleryGun import ArtilleryGun
from Target import Target

gun=ArtilleryGun()
target = Target()

for i in range(1, 340):
    gun.firingBarrage(target, 5)
# TODO an interactive firing mode