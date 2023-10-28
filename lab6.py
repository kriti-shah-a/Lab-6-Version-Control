# Kriti Shah and Matthew Toro

def main():
    condition = True

    while condition:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        user_input = int(input('Please enter an option: '))

        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded = encoder(password)
            print('Your password has been encoded and stored!')
            print()

        if user_input == 2:
            print('The encoded password is' + str(encoded) + ', and the original password is ' + str(decoder(encoded)) + '.')
            print()

        if user_input == 3:
            exit()


def encoder(password):
    x = []

    for i in range(0, len(password)):
        x.append(int(password[i])+3)

    return str(x)


def decoder(password):
    x = []

    for i in range(0, len(password)):
        x.append(int(password[i])-3)

    return str(x)


if __name__ == '__main__':
    main()