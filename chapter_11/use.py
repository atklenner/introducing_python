from zoo import hours as info
from collections import OrderedDict, defaultdict

info()

plain = {"a": 1, "b": 2, "c": 3}
for item in plain:
  print(item)

fancy = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
for item in fancy:
  print(item)

dict_of_lists = defaultdict(list)
dict_of_lists["a"] = "something for a"
print(dict_of_lists)