class V2:
 def __init__(self, x, y,
              x_attr="x",
              y_attr="y"):
  self._x_attr = x_attr
  self._y_attr = y_attr
  setattr(self, x_attr, x)
  setattr(self, y_attr, y)

 def __str__(self):
  return '<V2(%s, %s)>' % (
   self._x, self._y
  )

 def __repr__(self):
  return self.__str__()

 @property
 def _x(self):
  return getattr(self, self._x_attr)

 @property
 def _y(self):
  return getattr(self, self._y_attr)

 def __add__(self, other):
  return V2(self._x + other._x,
            self._y + other._y)

 def __sub__(self, other):
  return V2(self._x - other._x,
            self._y - other._y)

 def __mul__(self, other):
  return V2(self._x * other._x,
            self._y * other._y)

 def dot(self, other):
  if not isinstance(other, V2):
    raise TypeError(\
     'Both must be V2 objects.'\
    )
  return self._x * other._x + \
         self._y * other._y

 def __matmul__(self, other):
  return self.dot(other)

 def __rmul__(self, scalar):
  return self.__mul__(scalar)

 def __neg__(self):
  return V2(-self._x, -self._y)

 def __truediv__(self, scalar):
  return V2(self._x / scalar,
            self._y / scalar)

 def __mod__(self, scalar):
  return V2(self._x % scalar,
            self._y % scalar)

 def __abs__(self):
  return math.sqrt(
   self._x**2 + self._y**2)

 def distance_to(self, other):
   return abs(self - other)

 def to_polar(self):
  return self.__abs__(),\
         math.atan2(self._y, self._x)

