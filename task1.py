import random, string
n = 15
dif = input("Difficulty type (can be easy, medium or hard): ")
if dif != "easy" and dif != "medium" and dif != "hard":
    raise SyntaxError("input only these words: easy, medium or hard")
password=""
if dif == "easy":
    for i in range(n):
        password+=random.choice([random.choice(string.ascii_lowercase), str(random.randint(0,9))])
elif dif == "medium":
    for i in range(n):
        password+=random.choice([random.choice(string.ascii_letters), str(random.randint(0,9))])
else:
    for i in range(n):
        password+=random.choice([random.choice(string.ascii_letters), str(random.randint(0,9)), random.choice(string.punctuation)])
print("Generated password: "password)