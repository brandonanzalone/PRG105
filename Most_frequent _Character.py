def main():
    try:
        sentence = input('Please enter a senctence or statment of your choice. ')
        if not sentence:
            raise ValueError('Please enter a sentence or statment. ')
        calculate_characters(sentence)
    except ValueError as z:
        print(z)
#calculates the number of times a character appears
def calculate_characters(sentence):
    characters = {}
    for character in sentence:
        if character.isalnum():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1           
    find_frequent(characters)
#finds the most frequent character
def find_frequent(characters):
    mostfrequentletter = ''
    countofletter = 0
    for key, value in characters.items():
        if value > countofletter:
            countofletter = value
            mostfrequentletter = key
    print("The most frequent character found is ", mostfrequentletter)


main()

