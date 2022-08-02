# 10.1
from pickletools import read_int4
from traceback import print_tb


class Thing:
  pass

print(Thing)
example = Thing()
print(example)

# 10.2
class Thing2:
  letters = "abc"

print(Thing2.letters)

# 10.3
class Thing3:
  def __init__(self) -> None:
    self.letters = "xyz"

obj = Thing3()
print(obj.letters)

# 10.4-8
class Element:
  def __init__(self, name, symbol, number) -> None:
    self.__name = name
    self.__symbol = symbol
    self.__number = number
  
  @property
  def name(self):
    return self.__name

  @property
  def symbol(self):
    return self.__symbol

  @property
  def number(self):
    return self.__number

  def __str__(self):
    return f"{self.__name}, {self.__symbol}, {self.__number}"

dict = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**dict)
print(hydrogen)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# 10.9
class Bear:
  def eats(self):
    return "berries"

class Rabbit:
  def eats(self):
    return "clover"

class Octothorpe:
  def eats(self):
    return "campers"

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())

# 10.10
class Laser:
  def does(self):
    return "disintegrate"

class Claw:
  def does(self):
    return "crush"

class SmartPhone:
  def does(self):
    return "ring"

class Robot:
  def __init__(self) -> None:
    self.__laser = Laser()
    self.__claw = Claw()
    self.__smartphone = SmartPhone()

  def does(self):
    print(self.__laser.does())
    print(self.__claw.does())
    print(self.__smartphone.does())

robot = Robot()
robot.does()