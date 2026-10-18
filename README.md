CodeAlpha Python Programming Internship — Tasks

This repository contains three Python projects developed during my CodeAlpha Python Programming Internship. Each project focuses on a practical programming task and includes source code, documentation, and automated tests.

Task 1: Hangman Game

A command-line word-guessing game featuring random word selection, visual Hangman stages, input validation, duplicate-guess detection, six incorrect attempts, and replay functionality.

Run the game:

python Hangman/hangman.py

Run the tests:

python -m unittest discover -s Hangman/tests -v

Task 2: Stock Portfolio Tracker

A command-line application for managing stock holdings, recording quantities and manually provided prices, calculating portfolio investment totals, and saving portfolio data.

Run the application:

python StockPortfolio/stock_portfolio.py

Run the tests:

python -m unittest discover -s StockPortfolio/tests -v

Note: The application uses stored or manually entered prices rather than live stock-market data.

Task 3: File Organizer Automation

A Python utility that organizes files into category-based folders, including images, documents, videos, audio, archives, code, and other files.

Run the application:

python FileOrganizer/file_organizer.py

Run the tests:

python -m unittest discover -s FileOrganizer/tests -v

Repository Structure

codealpha_tasks/
├── Hangman/
│   ├── hangman.py
│   └── tests/
│       └── test_hangman.py
│
├── StockPortfolio/
│   ├── stock_portfolio.py
│   ├── tests/
│   │   └── test_stock_portfolio.py
│   ├── README.md
│   └── .gitignore
│
├── FileOrganizer/
│   ├── file_organizer.py
│   ├── tests/
│   │   └── test_file_organizer.py
│   ├── README.md
│   └── .gitignore
│
├── README.md
└── .gitignore

Technologies Used

- Python
- Python standard library
- "unittest" for automated testing
- Git and GitHub

Internship

Developed as part of the CodeAlpha Python Programming Internship.
