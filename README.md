# Sudoku

This is a Sudoku game implemented using Python and Pygame. The game allows users to select a difficulty level (Easy, Medium, Hard) and play a Sudoku puzzle. The game also includes a timer and the ability to display the solution.

## Features

- Select difficulty level: Easy, Medium, Hard
- Interactive Sudoku board
- Timer to track the time taken to solve the puzzle
- Display the solution

## Requirements

- Python 3.x
- Pygame
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Redinferno1736/sudoku.git
    cd sudoku
    ```

2. Install the required packages:
    ```sh
    pip install pygame requests
    ```

## Usage

1. Run the [app.py](http://_vscodecontentref_/1) file to start the game:
    ```sh
    python app.py
    ```

2. Select a difficulty level by clicking on one of the buttons (Easy, Medium, Hard).

3. Solve the Sudoku puzzle by clicking on the cells and entering numbers.

4. Click the "Solution" button to display the solution.

## File Structure

- [app.py](http://_vscodecontentref_/2): Main application file that initializes Pygame and handles the difficulty selection screen.
- [functions.py](http://_vscodecontentref_/3): Contains functions for fetching the Sudoku board, displaying the board, and handling user input.
- [sudoku_solver.py](http://_vscodecontentref_/4): Contains the Sudoku solver algorithm.
- [README.md](http://_vscodecontentref_/5): This file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Pygame](https://www.pygame.org/)
- [YouDoSudoku API](https://youdosudoku.com/api/)