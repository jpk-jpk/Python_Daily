def mysum(*numbz):
"""THIS PROGRAM IS USED FOR THE SUM OF THE NUMBERS
GIVEN WITH COMMA"""
    sumt = 0
    if len(numbz) > 0:
        for x in numbz:
            sumt += x
    print(sumt)
    return sumt


# if __name__ == "__main__":
#     print(mysum(25, 25, 65))
