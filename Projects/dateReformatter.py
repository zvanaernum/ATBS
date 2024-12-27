import pyperclip
import re


# Copy text from clipboard
text = str(pyperclip.paste())

# Make Regex Patterns for each date format
dateRegex1 = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')  # MM/DD/YYYY
dateRegex2 = re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')  # MM-DD-YYYY
dateRegex3 = re.compile(r'(\d{4})/(\d{1,2})/(\d{1,2})')  # YYYY/MM/DD

patterns = [dateRegex1, dateRegex2, dateRegex3] # store each regex in a list for eash iteration

# Function to standardize date format into YYYY-MM-DD
def standardizeDate(match, pattern):
    if pattern == dateRegex1 or pattern == dateRegex2:
        month, day, year = match.groups()  # Multiple assignment of month, day, year to the matched groups
    elif pattern == dateRegex3:
        year, month, day = match.groups()

    # Convert month and day to integers and format with leading zeros
    formattedMonth = f"{int(month):02d}"  # Pad the number with zeros if it has fewer than 2 digits adn assign
    formattedDay = f"{int(day):02d}"

    # Create the standardized date string in 'YYYY-MM-DD' format
    standardizedDate = f"{year}-{formattedMonth}-{formattedDay}"

    return standardizedDate

# Function to find and replace dates
def replaceDates(text, patterns):
    for pattern in patterns: # iterate through the list of patterns
        matches = pattern.finditer(text)  # Iterate through the text and find matches to the patterns, return match object
        for match in matches:
            standardizedDate = standardizeDate(match, pattern)
            originalDate = match.group(0)  # Get the entire matched string from the match object
            text = text.replace(originalDate, standardizedDate)
    return text

# Example usage with clipboard text
standardized_text = replaceDates(text, patterns)
print(standardized_text)
