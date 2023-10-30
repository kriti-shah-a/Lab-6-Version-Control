# Kriti Shah and Matthew Toro
#hello

def encoder(password):  # Encoder function, adding three
    new_password = ''

    for digit in password:  # all the digit in password

        if digit.isdigit():  # if the digits are a digit
            number = int(digit)  # the digit makes it into an integer = number
            encode = number + 3  # make the encode by adding three to the digits
            new_password += str(encode)  # turn each encoded digit to a string and add to the new password str

    return new_password  # return the new string

def decoded(password):  # Decoder function, inverse of encoder
    x = []
    y = ''

    for i in range(0, len(password)):  # for every index in password
        x.append(int(password[i]) - 3)  # minus 3 to every value in password and append to the list

    for i in x:  # in the new form list x with values minus 3, for every value of i in x
        y += str(i)  # add the i as a string to string y

    return y  # return the string that has subtracted 3 for each number

# hello

def main():
    while True:  # Loop function
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')  # Print the Menu
        user_input = int(input('Please enter an option: '))  # asking for user input

        if user_input == 1:  # Encoder option
            password = input('Please enter your password to encode: ')
            encoded = encoder(password)  # storing the password encoded
            print('Your password has been encoded and stored!')
            print()

        if user_input == 2:  # Decoder option
            # sharing the encoded password and using the decoder function
            print(f'The encoded password is {str(encoded)} and the original password is {str(decoded(encoded))}.')  #
            print()

        if user_input == 3:  # Exit function
            break


if __name__ == '__main__':  # Main
    main()