# import the necessary libaries and inputs
import re

# Dates to test the function

valid_date1 = '04/12/2004' # Regular date

valid_date2 = '29/02/2020' # Leap year

valid_date3 = '31/01/2019' # End of January

valid_date4 = '30/04/2018' # End of April

valid_date5 = '28/02/2021' # Non-leap year

invalid_month1 = '32/01/2000' # Invalid day

invalid_month2 = '31/04/2020' # April has only 30 days

invalid_day1 = '29/02/2021' # February has only 28 days in a non-leap year

invalid_day2 = '31/02/2020' # February never has 31 days

invalid_day3 = '00/12/2000' # Day cannot be zero

invalid_month3 = '01/13/2000' # Invalid month

invalid_month4 = '01/00/2000' # Month cannot be zero

invalid_year1 = '01/01/999' # Invalid year (less than 1000)

invalid_year2 = '01/01/3000' # Invalid year (greater than 2999)

# Define a regex to detect a date in the DD/MM/YYYY format and store  M, D, Y in variables
dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')  # DD/MM/YYYY
 
def dateMatch(input):
	mo = dateRegex.search(input)
	if mo:
		day, month, year = map(int, mo.groups())
		print(day, month, year)
		return day, month, year
	else:
		return None, None, None


# Sub function to determine if year is valid
def validYear(year):
	if 1000 <= year <= 2999:
		return True
	else:
		return False

# Sub function to determine if it is a leap year
def isLeapYear(year):
	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 == 0):
				return True
			else:
				return False
		else:
			return True
	else:
		return False
# Sub function to determine if the month is valid
def validMonth(month):
	if 1 <= month <= 12:
		return True
	else:
		return False

# Sub function to determine if the day is valid
def validDay(year, month, day):
    if month in [4, 6, 9, 11] and 1 <= day <= 30:
        return True
    elif month == 2:
        if isLeapYear(year) and 1 <= day <= 29:
            return True
        elif not isLeapYear(year) and 1 <= day <= 28:
            return True
    elif month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        return True
    else:
        return False


# Main function to determine if the date is valid
def isValidDate(input):
	day, month, year = dateMatch(input)
	
	if day is None or month is None or year is None:
		return False, 'Part of the date is missing'
	
	if not validYear(year):
		return False, 'Invalid year'
	
	if not validMonth(month):
		return False, 'Invalid Month'
	
	if not validDay(year, month, day):
		return False,'Invalid Day'
	
	return True, 'Date is Valid'



# Example usage with both the input date and the result
print(f"{valid_date1}: {isValidDate(valid_date1)}")  # Should return '04/12/2004: True'
print(f"{valid_date2}: {isValidDate(valid_date2)}")  # Should return '29/02/2020: True'
print(f"{valid_date3}: {isValidDate(valid_date3)}")  # Should return '31/01/2019: True'
print(f"{valid_date4}: {isValidDate(valid_date4)}")  # Should return '30/04/2018: True'
print(f"{valid_date5}: {isValidDate(valid_date5)}")  # Should return '28/02/2021: True'

print(f"{invalid_month1}: {isValidDate(invalid_month1)}")  # Should return '32/01/2000: False'
print(f"{invalid_month2}: {isValidDate(invalid_month2)}")  # Should return '31/04/2020: False'
print(f"{invalid_day1}: {isValidDate(invalid_day1)}")  # Should return '29/02/2021: False'
print(f"{invalid_day2}: {isValidDate(invalid_day2)}")  # Should return '31/02/2020: False'
print(f"{invalid_day3}: {isValidDate(invalid_day3)}")  # Should return '00/12/2000: False'
print(f"{invalid_month3}: {isValidDate(invalid_month3)}")  # Should return '01/13/2000: False'
print(f"{invalid_month4}: {isValidDate(invalid_month4)}")  # Should return '01/00/2000: False'
print(f"{invalid_year1}: {isValidDate(invalid_year1)}")  # Should return '01/01/999: False'
print(f"{invalid_year2}: {isValidDate(invalid_year2)}")  # Should return '01/01/3000: False'

