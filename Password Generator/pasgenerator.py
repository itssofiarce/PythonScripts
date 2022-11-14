import random


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(2, 4)

    # Eazy Level - Order not randomised:
    # password is a str
    # password = ""
    # in the advanced is a list password_list =""
    # # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    password_list = [random.choice(letters) for number_of_letter in range(1, nr_letters + 1)]+[random.choice(numbers)
                                                                                               for number_of_numbers in range(1, nr_numbers + 1)]+[random.choice(symbols) for number_of_symbols in range(1, nr_symbols + 1)]

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    # print(password_list)
    random.shuffle(password_list)
    # print(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    # print(f"Your password is: {password}")
    return password
