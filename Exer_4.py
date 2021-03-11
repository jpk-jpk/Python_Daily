def conv_hex():
    try:
        hex_n = str(input('Enter the hex number: '))
        print(f'The equivalent decimal number is: {int(hex_n, 16)}')
    except ValueError as e:
        print('Enter proper number: ', e)

    try:
        decn = 0
        hex_n = input('Enter the hex number: ')
        for p, d in enumerate(hex_n[::-1]):
            decn += int(d, 16) * (16 ** p)
        print(f'The equivalent decimal number is: {decn}')
    except ValueError as e:
        print('Enter proper number: ', e)


if __name__ == "__main__":
    conv_hex()
