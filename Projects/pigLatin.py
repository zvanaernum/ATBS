# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y') # tuple of strings

pigLatin = [] # Open a list variable to store the pig latin words
for word in message.split(): # split the phrase into individual words (a list of strings)
    # Separate the non-letters at the start of this word (i.e. punctuation marks):
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha(): # While character is not alpha
        prefixNonLetters += word[0] # add the non letters to a variable
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters) 
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha(): # while the last character in the word is not alpha
        suffixNonLetters = word[-1] + suffixNonLetters # add the non letter to a variable
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper() # evalautes to true or false
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = '' # open a new variable for prefix consonants
    while len(word) > 0 and not word[0] in VOWELS: # if letter is not in vowels
        prefixConsonants += word[0] # append to the veriable
        word = word[1:] # move on to the next letter in the word.

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '': # if prefixConsonants is not blank
        word += prefixConsonants + 'ay' # append the consonants and ay at the end of the word.
    else:
        word += 'yay' # else it starts with a vowel and yay shold be added to the end.

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))