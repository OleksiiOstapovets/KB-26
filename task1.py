import random, string
def Difficulty(dif):
    while True:
        if dif in ("easy", "medium", "hard"):
            return dif
        dif = str(input("Input only one of these words: easy, medium or hard: "))
def Creating_password(dif):
    n=15
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
    return password
if __name__ == "__main__":
    dif = Difficulty(str(input("Difficulty type (can be easy, medium or hard): ")))
    print(Creating_password(dif))
