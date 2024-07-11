# Darts

## Overview
The Darts class is designed to generate and display a matrix filled with concentric layers of numbers, resembling a dartboard. The size of the matrix is specified upon instantiation, and the matrix is populated such that the outermost layer is filled with 1s, the next layer with 2s, and so on, until the center is reached.

## Class Definition

*\__init__(self, size)*
The constructor initializes the Darts object with a given size.
- size (int): Specifies the dimensions of the square matrix (size x size).

*matrix(self)*
Creates an empty square matrix of the given size, filled with zeros.
- Returns: A size x size matrix initialized with zeros.

*to_darts(self)*
Generates the dartboard matrix by filling it with concentric layers of numbers.
- Returns: A size x size matrix with concentric layers filled with increasing integers starting from 1.

*\__str__(self)*
Provides a string representation of the dartboard matrix. Each row of the matrix is represented as a string of space-separated numbers, and rows are separated by newline characters.
- Returns: A string representation of the dartboard matrix.

## Usage
### Example
```
# Create a Darts object with a matrix size of 5
dartboard = Darts(5)

# Print the dartboard matrix
print(dartboard)
```
### Expected Output
For a matrix size of 5, the output will be:
```
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
```
### Explanation
The outermost layer (1s) forms the outer border of the matrix.
The next layer (2s) forms a square inside the outermost layer.
The innermost layer (3) is at the center of the matrix.

## Notes
- The matrix size must be a positive integer (<19).
- The class handles only square matrices.