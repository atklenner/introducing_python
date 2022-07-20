# 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.replace("moray", "Moray"))

# 5.2
questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]

print(questions[0], answers[1])
print(questions[1], answers[2])
print(questions[2], answers[0])

# 5.3
poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now he thinks he's a %s.""" % ("roast beef", "ham", "head", "clam")
print(poem)

# 5.4
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""

# 5.5
print(letter.format(salutation="Hello", name="Andrew",
                    product="diapers", verbed="exploded", 
                    room="garage", amount="one million dollars", 
                    animals="otters", percent="100", 
                    spokesman="Richard Gere", job_title="Peon"))

# 5.6
print("%sy Mc%sface" % ("Duck", "Duck"))
print("%sy Mc%sface" % ("Gourd", "Gourd"))
print("%sy Mc%sface" % ("Spitz", "Spitz"))

# 5.7
print("{}y Mc{}face".format("Duck", "Duck"))
print("{}y Mc{}face".format("Gourd", "Gourd"))
print("{}y Mc{}face".format("Spitz", "Spitz"))

# 5.8
duck = "Duck"
print(F"{duck}y Mc{duck}face")
gourd = "Gourd"
print(F"{gourd}y Mc{gourd}face")
spitz = "Spitz"
print(F"{spitz}y Mc{spitz}face")