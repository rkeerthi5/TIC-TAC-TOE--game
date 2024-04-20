# Tic Tac Toe Game

This is a simple implementation of the Tic Tac Toe game using Python's tkinter library for the GUI.

## How to Play

1. *Setup*: Run the script, and a window titled "Tic Tac Toe" will appear.
2. *Game Interface*: The game interface consists of a 3x3 grid of buttons.
3. *Gameplay*: Players take turns clicking on the buttons to place their symbol (either "X" or "O") on the grid.
4. *Winning Condition*: The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
5. *Draw Condition*: If all spaces on the grid are filled and no player has won, the game ends in a draw.

## Features

- Simple and intuitive GUI.
- Automatic detection of winning and draw conditions.
- Ability to reset the game after completion.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing this code.
3. Navigate to the directory where the code is located.
4. Run the following command in your terminal or command prompt:
   
   python app.py
   

## Code Structure

- TicTacToe class: Manages the game logic and GUI using tkinter.
- create_board: Initializes the game board with buttons.
- button_click: Handles button click events and updates the game state accordingly.
- toggle_player: Switches between "X" and "O" players after each move.
- check_winner: Checks if there is a winner based on the current board state.
- check_draw: Checks if the game has ended in a draw.
- reset_game: Resets the game board and player turns after a game ends.

Feel free to explore and modify the code to add more features or customize the game as you like!
