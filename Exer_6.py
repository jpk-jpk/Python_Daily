from Exer_5 import piglatin


def pl_ss(sente):
    pl_s = []
    for word in sente.split():
        pl_s.append(piglatin(word))
    print(" ".join(pl_s))


if __name__ == "__main__":
    pl_ss('Hello I am pradeep Kumar')
