# Futoshiki_Puzzle
# Overview
This project is a Python-based implementation of the Futoshiki puzzle game using the tkinter library for the graphical user interface (GUI) and pygame for sound effects. The game allows users to play Futoshiki puzzles of varying sizes (4x4, 5x5, 6x6) and provides features like hints, solution checking, and puzzle clearing.

# Features
  * Multiple Puzzle Sizes: Choose from 4x4, 5x5, or 6x6 grid sizes.
  * Hints: Get hints to fill in the correct number in a selected cell (limited to 3 hints per game).
  * Solution Checking: Check if the current entries are correct.
  * Show Solution: Reveal the complete solution to the puzzle.
  * Clear Puzzle: Clear all user inputs and reset the puzzle to its initial state.
  * Sound Effects: Play sound effects for button clicks and game events.

# Requirements
  * Python 3.x
  * tkinter (usually comes pre-installed with Python)
  * pygame (for sound effects)

# Installation
  * Install Dependencies:
  pip install pygame
  * Run the Game:
  python futoshiki.py
# How to Play
  * Start the Game: Click the "Play" button on the main window.
  * Choose Puzzle Size: Select the size of the puzzle you want to play (4x4, 5x5, or 6x6).
  * Understand the Rules: Click the "Rules" button to understand how to play Futoshiki.
  * Fill the Grid: Enter numbers in the empty cells following the rules of Futoshiki.
  * Use Hints: If you're stuck, use the "Hint" button to reveal a correct number (limited to 3 hints).
  * Check Your Solution: Use the "Check" button to verify if your entries are correct.
  * Show Solution: If you want to see the complete solution, click the "Show Solution" button.
  * Clear Puzzle: To reset the puzzle, click the "Clear" button.
  * New Game: Start a new game by clicking the "New Game" button.
# Code Structure
  * Main Window: The first window that appears when you run the game. It contains the "Play" button.
  ![Screenshot 2023-08-08 133633](https://github.com/user-attachments/assets/ec940b85-d939-4ec5-99b3-816ebc7f5190)
  * Second Window: Appears after clicking "Play". It contains buttons to view rules and choose puzzle size.
  ![Screenshot 2023-08-08 133730](https://github.com/user-attachments/assets/b07c8b87-2641-4ac2-a316-30e7b5f7c90b)
  * Rules Window: Displays the rules of Futoshiki.
  ![Screenshot 2023-08-08 133920](https://github.com/user-attachments/assets/a8b7b7ca-0d46-413e-9f54-d3521fd5c865)
  * Choose Window: Allows the user to select the puzzle size.
  ![Screenshot 2023-08-08 134004](https://github.com/user-attachments/assets/abafbdec-ff45-4553-896b-1c451a3bb91f)
  * Question Window: The main game window where the puzzle is displayed and solved.
  ![Screenshot 2023-08-08 124641](https://github.com/user-attachments/assets/49ccd7a5-c8c8-4a2a-a5d5-6707a9e77a02)
# Functions
  * open_second_window(): Opens the second window with options to view rules or choose puzzle size.
  * open_rules_window(): Displays the rules of Futoshiki.
  * open_choose_window(): Allows the user to choose the puzzle size.
  * on_play(n): Starts the game with the selected puzzle size.
  * answer(n): Generates a random Futoshiki puzzle of size n x n.
  * is_valid(puzzle, row, col, num): Checks if a number is valid in a given cell.
  * solve_puzzle(puzzle, numbers, row=0, col=0): Solves the Futoshiki puzzle using backtracking.
