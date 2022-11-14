import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("Nato Alphabet/nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


user_word_loop = True
while user_word_loop:

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    user_word = input("Enter a word: ").upper()
    if user_word == "EXIT":
        print("goodbye!")
        user_word_loop = False
    else:
        try:
            user_code = [nato_dic[letter] for letter in list(user_word)]
        except KeyError:
            print("Sorry, Only Letters please")
        else:
            print(user_code)
