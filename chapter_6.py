# 6.1
for i in [3, 2, 1, 0]:
  print(i)

# 6.2
guess_me = 7
number = 1
while True:
  if number < guess_me:
    print("too low")
  elif number > guess_me:
    print("oops")
    break
  elif number == guess_me:
    print("found it!")
    break
  number += 1

# 6.3
guess_me = 5
for number in range(10):
  if number < guess_me:
    print("too low")
  elif number == guess_me:
    print("found it!")
    break
  elif number > guess_me:
    print("oops")
    break