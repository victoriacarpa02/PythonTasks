# Coordinates

## Overview
The Coordinates class is designed to validate geographical coordinates from input data. It checks if each line of input contains valid latitude and longitude values. Latitude must be between -90 and 90 degrees, and longitude must be between -180 and 180 degrees.
## Class Definition

*\__init__(self, data)*
The constructor initializes the Coordinates object with the input data.
- data (iterable): An iterable object (like sys.stdin) containing lines of input data.

*is_true_coordinates(self)*
This method validates each line of coordinates.
- Returns: A list of strings where each string is 'True' if the corresponding line contains valid coordinates, otherwise 'False'.

*\__str__(self)*
Provides a string representation indicating whether each line of input data contains valid coordinates. Each result is on a new line.
- Returns: A string with 'True' or 'False' for each line of input, separated by newlines.

## Usage
### Example
```
34.05 -118.25
91 181
-45.0 120.5
```
### Expected Output
For the above input, the expected output will be:
```
True
False
True
```
### Explanation
The first line 34.05 -118.25 is valid (True) because 34.05 is between -90 and 90, and -118.25 is between -180 and 180.
The second line 91 181 is invalid (False) because 91 is not between -90 and 90, and 181 is not between -180 and 180.
The third line -45.0 120.5 is valid (True) because -45.0 is between -90 and 90, and 120.5 is between -180 and 180.

## Notes
- The input data must be an iterable that provides lines of text (e.g., sys.stdin, a list of strings, or a file object).
- The class uses regular expressions to extract numerical values from each line.
- The latitude and longitude values must be properly formatted as floating-point or integer numbers.
- This class does not handle other formats or types of coordinate systems.