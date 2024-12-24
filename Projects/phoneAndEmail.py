#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code with or without parenthesis
    (\s|-|\.)?                        # separator space hyphen or dot
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator space hyphen or dot
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension optional
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
       areaCode = groups[1] if groups[1] else "" # assign group 1 to areaCode. If empty, assign blank string
       areaCode = areaCode.replace('(', '').replace(')', '') # if area code has parenthesis, remove them replace with empty string
       phoneNum = '-'.join([areaCode, groups[3], groups[5]]) # jpin the numbers with hyphens
       if groups[8] != '':
           phoneNum += ' x' + groups[8] # if extension is found, append extension
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0]) # append the enetire email tuple (group index 0)

# Copy results to the clipboard:
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
      print('No phone numbers or email addresses found')