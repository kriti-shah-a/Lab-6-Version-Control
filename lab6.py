# Kriti Shah and Matthew Toro
def encoder(password):  # Encoder function, returns encoded password
    x = []  # empty list
    y = ''  # empty string

    for i in range(0, len(password)):  # for every index in password
        x.append(int(password[i]) + 3)  # add 3 to every value in password and append to the list

    for i in x:  # in the new form list x with values add 3, for every value of i in x
        y += str(i)  # add the i as a string to string y

    return y  # return the string that has added 3 for each number


def decoded(password):  # Decoder function, inverse of encoder
    x = []
    y = ''

    for i in range(0, len(password)):  # for every index in password
        x.append(int(password[i]) - 3)  # minus 3 to every value in password and append to the list

    for i in x:  # in the new form list x with values minus 3, for every value of i in x
        y += str(i)  # add the i as a string to string y

    return y  # return the string that has subtracted 3 for each number


def main():   # the main function
    condition = True

    while condition:  # Loop function
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')  # Print the Menu
        user_input = int(input('Please enter an option: '))  # asking for user input

        if user_input == 1:  # Encoder option
            password = input('Please enter your password to encode: ')
            encoded = encoder(password)  # storing the password encoded
            print('Your password has been encoded and stored!')
            print()

        if user_input == 2:  # Decoder option
            print('The encoded password is ' + str(encoded) + ', and the original password is ' + str(
                decoded(encoded)) + '.')  # sharing the encoded password and using the decoder function
            print()

        if user_input == 3:  # Exit function
            exit()


if __name__ == '__main__':  # Main
    main()
