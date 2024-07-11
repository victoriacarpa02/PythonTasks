# Fourth Thursday of the Month

## Overview
The FourthThursday class is designed to find and display the date of the fourth Thursday of a given month and year. This can be useful for scheduling events, meetings, or any activities that recur on the fourth Thursday of each month.
## Class Definition

*\__init__(self, year, month)*
The constructor initializes the FourthThursday object with a given year and month.
- year (int): The year for which to find the fourth Thursday.
- month (int): The month for which to find the fourth Thursday.

*right_day(self)*
This property calculates the exact date of the fourth Thursday of the specified month and year.
- Returns: A date object representing the fourth Thursday of the month.

*\__str__(self)*
Provides a string representation of the date of the fourth Thursday in the format dd.mm.yyyy.
- Returns: A string formatted as dd.mm.yyyy representing the fourth Thursday of the month.

## Usage
### Example
```
2024
7
```
### Expected Output
For the input year 2024 and month 7 (July), the output will be:
```
25.07.2024
```
### Explanation
The program calculates the dates for each week of the specified month using calendar.monthcalendar.
It checks the fourth Thursday by examining the month calendar matrix:

- If the first Thursday of the month appears in the first week, the fourth Thursday is in the fourth week. Otherwise,
  the fourth Thursday is in the fifth week.

The \__str__ method formats this date in dd.mm.yyyy format for easy reading.

## Notes
- The month should be an integer between 1 and 12.
- The year should be a valid integer representing a calendar year.
- The program uses the Gregorian calendar system.
- Make sure the input year and month are valid to avoid runtime errors.