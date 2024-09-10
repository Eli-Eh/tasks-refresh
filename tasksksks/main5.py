def game(g):
    if g==70:
        return True
    else:
        return False

for i in range(3):
    g=int(input("guess: "))

    if game(g):
        print("done")
        break
    else:
        print("no")