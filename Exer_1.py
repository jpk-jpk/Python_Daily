import random


def guess_game():
    guess_no = random.randint(0, 100)
    while True:
        try:
            guess_user = int(input('Guess the number: '))
        except ValueError as e:
            print(f"The error raised is {e}")
            break

        if guess_user > guess_no:
            print('Enter lower number')
        elif guess_user < guess_no:
            print('Enter higher value')
        else:
            print('You entered correct number')
            break


if __name__ == "__main__":
    guess_game()
