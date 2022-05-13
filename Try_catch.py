class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car,Car):
      raise TypeError(f'{car.model} is not a {car.__class__.__name__} object')
    self.cars.append(car)

"""
We would use these classes in this way:
"""

Ford = Garage()
Fiesta = Car('Ford','Fiesta')
#Ford.add_car(Fiesta)

try:
  Ford.add_car(Fiesta)
except TypeError:
  print('Inavlid object type while passing not a car object')
finally:
  print(f'Number of Car added {len(Ford)} !!')