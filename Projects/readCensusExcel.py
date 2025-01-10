#! python3
# readcensusExcel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint, os

workbookPath = os.path.join('automate_online-materials', 'censuspopdata.xlsx')
resultPath = os.path.join('Files', 'census2010.py')
print('Opening workbook....')
wb = openpyxl.load_workbook(workbookPath)
sheet = wb.active

countyData = {}
# Fill in countyData with each county's population and tracts
print('Reading rows...')
for row in range (2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    countyData.setdefault(state, {}) # write the state to the dictionary keys if it does not exists
    # If county for current state does not exist, write the key with placeholder tracts and pop values
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # Each row represents one census tract, so increment it by 1
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in the given census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open(resultPath, 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()