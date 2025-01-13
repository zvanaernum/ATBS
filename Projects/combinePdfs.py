#! python 3
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF.

import PyPDF2, os

openPath = os.path.join('Files') # set the folder to check for pdfs
savePath = os.path.join('Files', 'allminutes.pdf') 

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(openPath): # get all of the pdf files from the 'Files' folder
    if filename.endswith('.pdf'):
        pdfFiles.append(filename) # add all the pdf filenames to the pdfFiles list

pdfFiles.sort(key = str.lower) # sort the pdfFiles list 

pdfWriter = PyPDF2.PdfFileWriter() # create a new writer object

# Loop through all of the pdf files
for filename in pdfFiles:
    pdfFileObj = open(os.path.join(openPath, filename), 'rb') # open the pdf file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # create a reader object containing the file data

    # Loop through all of the pages (except for the first page) and add them to writer object
    for pageNum in range (1, pdfReader.numPages): # iterate through all pages skipping the first
        pageObj = pdfReader.getPage(pageNum) # create a page object that contains the page
        pdfWriter.addPage(pageObj) # add the page to the pdf writer.

# Save the resulting PDF to a file
pdfOutput = open(savePath, 'wb') # open a new pdf file in write binary mode
pdfWriter.write(pdfOutput)
pdfOutput.close()
