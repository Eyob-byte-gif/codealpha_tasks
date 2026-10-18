CodeAlpha Python Programming Internship — Tasks

This repository contains three Python projects developed during my CodeAlpha Python Programming Internship. Each project includes source code, documentation, and automated tests where applicable.

Task 1: Hangman Game

A command-line word-guessing game with random word selection, visual Hangman stages, input validation, duplicate-guess detection, six incorrect attempts, and replay functionality.

Run the game:

python Hangman/hangman.py

Run the tests:

python -m unittest discover -s Hangman/tests -v

Task 2: Stock Portfolio Tracker

A command-line application for managing stock holdings, recording quantities and manually provided prices, calculating portfolio investment totals, and saving portfolio data.

Project folder: "StockPortfolio/"

Run the application:

cd StockPortfolio
python stock_portfolio.py

Run the tests from the repository root:

python -m unittest discover -s StockPortfolio/tests -v

Note: The application uses stored or manually entered prices, not live stock-market data.

Task 3: File Organizer Automation

A Python utility that organizes files into category-based folders, including images, documents, videos, audio, archives, code, and other files.

Project folder: "FileOrganizer/"

Run the application:

cd FileOrganizer
python file_organizer.py

Run the tests from the repository root:

python -m unittest discover -s FileOrganizer/tests -v

Repository Structure

codealpha_tasks/
├── hangman.py
├── tests/
├── StockPortfolio/
│   ├── stock_portfolio.py
│   └── tests/
├── FileOrganizer/
│   ├── file_organizer.py
│   └── tests/
└── README.md

Each project folder also contains its own README and ".gitignore" file.

Technologies Used

- Python
- Python standard library
- "unittest" for automated testing
- Git and GitHub

Internship

Developed as part of the CodeAlpha Python Programming Internship.
