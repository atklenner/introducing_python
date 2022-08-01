from distutils import file_util


class Fruit:
  color = "red"

blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = "blue"
print(blueberry.color)
print(Fruit.color)

Fruit.color = "orange"
print(Fruit.color)
print(blueberry.color)
del blueberry.color
print(blueberry.color)

new_fruit = Fruit()
print(new_fruit.color)