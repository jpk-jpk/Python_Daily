def piglatin(word):
    word = word.upper()
    if word[0] in "aeiouAEIOU":
        return f'{word}way'
    else:
        return f"{word[1:] + word[0]}ay"


if __name__ == "__main__":
    print(piglatin('Hello'))
