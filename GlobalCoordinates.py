class Global:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        #self.pos = (self._x, self._y)
        #self.posz = (self._x, self._y, self._z)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, xcoord: float):
        self._x = xcoord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, ycoord: float):
        self._x = ycoord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, zcoord: float):
        self._z = zcoord

    @property
    def pos(self):
        return tuple((self._x, self._y))

    @pos.setter
    def pos(self, xytuple: tuple[float, float]):
        self._x = xytuple[0]
        self._y = xytuple[1]

    @property
    def posz(self):
        return tuple((self._x, self._y, self._z))

    @posz.setter
    def posz(self, xyztuple: tuple[float, float, float]):
        self._x = xyztuple[0]
        self._y = xyztuple[1]
        self._z = xyztuple[2]
