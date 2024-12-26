import pyperclip
import csv


# Define the file path for the output csv
outputFilePath = r'word_counts.csv'

text = str(pyperclip.paste())

def wordCount(text):
    count = {}
    words = text.split()
    for word in words:
        word = word.lower() # convert to lower case to handle case insensitivty
        word = word.strip(",.?!") # remove punctuation
        if word.isalpha(): # check if the words consists of only letters
            if word not in count:
                count.setdefault(word, 1)
            else: 
                count[word] = count[word] + 1 # if word already present, increment the value by 1

    # Write the dictionary to a csv file
    with open(outputFilePath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count']) # Write the header
        for word, count in count.items():
            writer.writerow([word, count])

    return count


print(wordCount(text))

