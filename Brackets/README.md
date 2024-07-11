# Brackets

## Overview
The Bracket class is designed to check whether a string of parentheses is balanced. A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis and the pairs are properly nested.

## Class Definition

*\__init__(self, brackets)*
The constructor initializes the Bracket object with a given string of parentheses.- size (int): Specifies the dimensions of the square matrix (size x size).
- *brackets (str): A string consisting of parentheses ( and ).*

*is_true(self)*
This method checks the given string of parentheses for balanced pairs. It repeatedly removes any balanced pair () from the string until no more balanced pairs can be found.
- Returns: The remaining string after all possible balanced pairs have been removed.

*\__str__(self)*
Generates the dartboard matrix by filling it with concentric layers of numbers.
- Returns: 'True' if the string is balanced, otherwise 'False'.

## Usage
### Example
```
# Create a Bracket object with a string of parentheses
user_input = Bracket("(()())")

# Print whether the string of parentheses is balanced
print(user_input)
```
### Expected Output
For the input string "(()())", the output will be:
```
True
```
### Another example
```
# Create a Bracket object with a string of parentheses
user_input = Bracket("(()")

# Print whether the string of parentheses is balanced
print(user_input)
```
### Expected Output
For the input string "(()", the output will be:
```
False
```
### Explanation
The string "(()" is not balanced because there is one opening parenthesis without a corresponding closing parenthesis.
The is_true method will remove one pair () and leave "(".
The __str__ method will then return 'False' as the final string is not empty.

## Notes
- The input string must only contain the characters ( and ).
- This class handles only parentheses and does not consider other types of brackets.