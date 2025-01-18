#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current working directory.

import csv, os

directoryPath = os.path.join('Files', 'removeCsvHeader_copy')
os.chdir(directoryPath) # change the working directory to the directory path with the files

os.makedirs('headerRemoved', exist_ok=True) # create a header removed folder where files will be saved

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file into a reader object (skipping first row).
    csvRows = [] # open an empty list for the rows data
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row in the csv file
        csvRows.append(row) # add csv rows to the empty list
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='') # open a new file with the sanme name
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()