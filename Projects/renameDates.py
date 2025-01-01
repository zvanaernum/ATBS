#! python3
# renameDates.py - Renames filenames with the American date format to European date format DD-MM-YYYY

import shutil, os, re

# create a regex to match file nanmes with American stype date formats 
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month                      
    ((0|1|2|3)?\d)-                 # one or two digits for the day   
    ((19|20)\d\d)                   # four digits for the year 
    (.*?)$                          # all text after the date                      
        """, re.VERBOSE)

# directory containing files:
p = r"C:\Users\Zac\OneDrive\Python\Practice\ATBS\Files\Test Files"

# Loop over the files in the working directory.
for amerFilename in os.listdir(p):
    mo = datePattern.search(amerFilename)
    # Skip files without a date
    if mo == None:
        continue
    # Get the different parts of the file name
    beforePart = mo.group(1)
    monthPath = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPath + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(p)
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename) # uncomment after testing