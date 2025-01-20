#! python3
# excelToCsv.py - converts all excel files in a directory to csv, including workbooks with multiple sheets

import os, csv, openpyxl

directoryPath = os.path.join('Files', 'ExcelFiles')
csvDirectoryPath = os.path.join('Files', 'csvFiles') # create a new folder for the csv files

# Create the CSV files directory if it doesn't exist 
if not os.path.exists(csvDirectoryPath):
    os.makedirs(csvDirectoryPath)

xlsxFiles = []
for excelFile in os.listdir(directoryPath):
    if excelFile.endswith('.xlsx'): # Skip non-xlsx files, load the workbook object.
        xlsxFiles.append(excelFile)
    wb = openpyxl.load_workbook(os.path.join(directoryPath, excelFile)) # create a workbook object
    excelFileName, _ = os.path.splitext(excelFile) # split off the file extension. Returns a tuple with the comma used to unpack into two variables (tuple unpacking)

    for sheetName in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]
        
        # Create the CSV filename from the Excel filename and sheet title.
        csvName = f"{excelFileName}_{sheetName}.csv" # create the csv file name with sheet name included
        csvFileObj = open(os.path.join(csvDirectoryPath, csvName), 'w', newline= '') # create a new folder called csvFiles and store new files there
        
        # Create the csv.writer object for this CSV file.
        csvWriter = csv.writer(csvFileObj)
        
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                cellValue = sheet.cell(row=rowNum, column=colNum).value
                rowData.append(cellValue)

            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)

        csvFileObj.close()