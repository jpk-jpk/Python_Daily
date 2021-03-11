def ubbi(word):
    t = []
    for e in word.upper():
        if e in "aeiouAEIOU":
            t.append(f"ub{e}")
        else:
            t.append(e)
    return "".join(t)


if __name__ == "__main__":
    print(ubbi('elephant'))
