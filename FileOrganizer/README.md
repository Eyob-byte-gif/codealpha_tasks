
# Python File Organizer

A command-line file organizer built with Python for the CodeAlpha Python Programming Internship.

## Features

- Sorts files into folders by extension
- Supports images, documents, videos, audio, archives, and code files
- Places unrecognized file types in an Others folder
- Creates category folders automatically
- Avoids overwriting files with duplicate names
- Handles invalid folder paths
- Includes automated tests using unittest

## Requirements

- Python 3
- No third-party packages required

## Run

```bash
python file_organizer.py
```

Enter the path of the folder you want to organize when prompted.

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
CodeAlpha_Automation/
├── file_organizer.py
├── README.md
├── test_files/
└── tests/
    └── test_file_organizer.py
```

## Safety Note

Test on a sample folder before organizing important files. The program moves files, so check the selected folder carefully.

## Technologies

Python, pathlib, shutil, unittest, Git, and GitHub.

