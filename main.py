import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data.to_dict())

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def code():
    input_word = input("What word needs coding?: ").upper()

    try:
        nato_code = [nato_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        code()
    else:
        print(nato_code)


code()
