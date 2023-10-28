# Kriti Shah and Matthew Toro

def main():
    condition = True

    while condition:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        user_input = int(input('Please enter an option: '))

        if user_input == 1:
            password = int(user_input('Please enter your password to encode: '))
            password = encoder(passworod)
            print('Your password has been encoded and stored!')
            print()


def encoder(password):
    for i in range(0, len(password)):
        if password[i].isdigit():
            password[i] += 3

    return password


def decoder(password):
    for i in range(0, len(password)):
        if password[i].isdigit():
            password[i] -= 3

    return password


if __name__ == '__main__':
    main()