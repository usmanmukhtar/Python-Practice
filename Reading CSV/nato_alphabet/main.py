import pandas
def main():
    """
    TODO 1: Create a dictionary in this format

    {
        'U': 'Uniform',
        'S': 'Sierra',
    }

    TODO 2: Create a list of the phonetic code words from a word that the user inputs

    [U, Uniform, S, Sierra, ...]
    """

    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    name = input('Please enter your name: ').upper()

    # TODO 1

    phonetic_alphabets = {row.letter: row.code for index, row in data.iterrows()}

    # TODO 2

    word_converter = [phonetic_alphabets[letter] for letter in name]

    print(word_converter)




if __name__ == '__main__':
    main()