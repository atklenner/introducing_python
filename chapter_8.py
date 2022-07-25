# 8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}

# 8.2
print(e2f["walrus"])

# 8.3
f2e = {value: key for (key, value) in e2f.items()}
print(f2e)

# 8.4
print(f2e["chien"])

# 8.5
for word in e2f.keys():
  print(word)

# 8.6
life = {"animals": {"cats": ["Henri", "Grumpy", "Lucy"], "octopi": {}, "emus": {}}, "plants": {}, "other": {}}

# 8.7
print(life.keys())

# 8.8
print(life["animals"].keys())

# 8.9
print(life["animals"]["cats"])

# 8.10
squares = {value: value * value for value in range(10)}
print(squares)

# 8.11
odd = {i for i in range(10) if i % 2 == 1}
print(odd)

# 8.12
# the questions in this book suck, no one proofread them, bad editing, thank god I pirated it

# 8.13
key = ("optimist", "pessimist", "troll")
value = ("The glass is half full", "The glass is half empty", "How did you get a glass?")
print(dict(zip(key, value)))

# 8.14
titles = ["Creature of Habbit", "Crewel Fate", "Sharks on a Plane"]
plots = ["A nun turns into a monster", "A haunted yarn shop", "Check you exits"]
print(dict(zip(titles, plots)))