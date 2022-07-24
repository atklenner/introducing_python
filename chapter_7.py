# 7.1
years_list = [1994, 1995, 1996, 1997, 1998, 1999]

# 7.2
print(years_list[3])

# 7.3
print(years_list[-1])

#7.4
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
things[1].capitalize()
print(things)

# 7.6
things[0] = things[0].upper()
print(things)

# 7.7
del things[2]
print(things)

# 7.8
surprise = ["Groucho", "Chico", "Harpo"]

# 7.9
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise)

# 7.10
even = [number for number in range(10) if number % 2 == 0]
print(even)

# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"

# my first answer but not the best one
# for (first, second) in rhymes:
#     first_line = ""
#     for start in start1:
#         first_line += start.capitalize() + "! "
#     first_line += first.capitalize() + "!"
#     print(first_line)
#     print(start2, second + ".")

first_line = " ".join([word.capitalize() + "!" for word in start1])
for (first, second) in rhymes:
    print(f"{first_line} {first.capitalize()}!")
    print(f"{start2} {second}.")