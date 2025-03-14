#! python 3
# mcb.py - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves keyword to clipboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # if index 1 of command line argument is save
    mcbShelf[sys.argv[2]] = pyperclip.paste() # then the second argument is the keyword for the content on the clipbaoard and value = text on clipboard

elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list': #if index 1 of argument is list, copy the keywords to the clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]]) # else, assume the argument is a keyword. If this keyword exists in mcbshelf, copy the value onto the clipboard.

mcbShelf.close()