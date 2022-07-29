# 9.1
from itertools import count


def good():
  return ["Harry", "Ron", "Hermione"]

good()

# 9.2
def get_odds():
  for i in range(10):
    if i % 2 == 1:
      yield i

count = 0
for i in get_odds():
  if count == 2:
    print("The third odd number is", i)
  count += 1

# 9.3
def test(func):
  def new_func(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return new_func

@test
def hello():
  print("Hello")

hello()

# 9.4
class OopsException(Exception):
  pass

# raise OopsException()

try: #try this code block
  raise OopsException("panic") # raises an exception called OopsException
except OopsException as exc: # looks for an OopsException to be raised, whatever is passed to it is called exc
  print(exc) # print exc