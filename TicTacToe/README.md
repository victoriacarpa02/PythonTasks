# Tic-Tac-Toe Game

This project implements a simple console-based Tic-Tac-Toe game in Python. The game allows two players to take turns marking spaces in a 3×3 grid, aiming to be the first to get three of their marks in a horizontal, vertical, or diagonal row.
Features
- Interactive console-based gameplay.
- Turn-based marking for two players.
- Automatic detection of the game winner or a draw.

## Classes and Methods
### 1. TicTacToe Class

The TicTacToe class is the main class that manages the game state, player turns, and game logic.
### 2. \__init__(self)
Initializes a new game:
- Sets up an empty 3x3 game board.
- Initializes the turn counter.

### 3. show(self)
Displays the current game board:
```
game = TicTacToe()
game.show()
```
**Output**:
```
 | | 
-----
 | | 
-----
 | | 
```
### 4. mark(self, n, m)

Marks a cell on the board for the current player:
- n (int): Row number (1-3).
- m (int): Column number (1-3).
```
game.mark(1, 1)  # Marks the top-left cell for the current player
```
- Checks if the game is already won or drawn.
- Alternates between 'X' and 'O' based on the turn.
- Prevents marking an already marked cell.

### 5. winner(self)
Checks for a winner or a draw:
- Returns 'X' or 'O' if a player has won.
- Returns 'Draw' if the game is a draw.
- Returns None if the game is still ongoing.

## Example Usage
Below is an example of how to use the TicTacToe class to play a game.
```
game = TicTacToe()

# Display the initial empty board
game.show()

# Players take turns marking the board
game.mark(1, 1)
game.show()

game.mark(1, 2)
game.show()

game.mark(2, 1)
game.show()

game.mark(1, 3)
game.show()

game.mark(3, 1)
game.show()

# Check for a winner
if game.winner():
    print(f'Winner: {game.winner()}')
else:
    print('The game continues')
```
**Output:**
```
 | | 
-----
 | | 
-----
 | | 

X| | 
-----
 | | 
-----
 | | 

X|O| 
-----
 | | 
-----
 | | 

X|O| 
-----
X| | 
-----
 | | 

X|O|O
-----
X| | 
-----
 | | 

X|O|O
-----
X| | 
-----
X| | 

Winner: X

```
