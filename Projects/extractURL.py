# This script will extract URLs from a copied block of text and return them to the clipboard
import pyperclip, re

urlRegex = re.compile(r'''(
    http[s]?://                 # HTTP or HTTPS
    (www\.)?                    # optional www.
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    (/[a-zA-Z0-9._%+-]*)*       # optional path or multiple paths
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in urlRegex.findall(text):
    matches.append(groups[0])  # append the entire URL

# Copy results to the clipboard and print them:
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs found')
