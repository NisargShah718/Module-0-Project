def word_frequency(word):
    frequency = {}
    list_of_letters = []
    for letter in word:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in list_of_letters:
                list_of_letters.append(letter)
                frequency[letter] = 1
            else:
                frequency[letter] += 1
    return(frequency)

print(word_frequency("Hello World! 123"))
