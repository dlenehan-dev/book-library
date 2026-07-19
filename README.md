# Book Library

## Overview

Book Library is a command-line application written in Python that allows users to manage a collection of books stored in an SQLite database.

The project was developed as part of a structured Python learning programme with an emphasis on writing clean, maintainable code, using Git effectively, and building automated tests with pytest.

---

## Features

* Add new books
* View all books
* Find a book by ID
* Update existing books
* Delete books
* Input validation
* Formatted console output
* Automated unit tests using pytest
* SQLite database for persistent storage

---

## Technologies Used

* Python 3
* SQLite
* pytest
* Git

---

## Project Structure

```
book-library/
│
├── main.py              # Application entry point
├── database.py          # Database operations
├── validation.py        # Input validation
├── ui.py                # Display formatting
├── books.db             # SQLite database
├── requirements.txt
│
└── tests/
    └── test_database.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd book-library
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the application with:

```bash
python main.py
```

The application will automatically create the database and required table if they do not already exist.

---

## Running the Tests

Execute the test suite with:

```bash
pytest
```

---

## What I Learned

This project provided practical experience with:

* Python functions and modules
* SQLite database programming
* CRUD operations
* Input validation
* Code refactoring
* Separation of responsibilities
* Writing unit tests with pytest
* Virtual environments
* Git and GitHub workflows

---

## Future Improvements

Possible enhancements include:

* Search books by title or author
* Prevent duplicate book entries
* Record publication year and genre
* Export the library to CSV
* Build a graphical user interface
* Develop a REST API
* Add logging and configuration files

---

## Author

Developed as part of a Python software development learning journey, applying previous software engineering experience to modern Python development.


Expanded README:
## Initial Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd book-library
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

The command prompt should now begin with:

```text
(.venv)
```

### 4. Install project dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify the installation

Check the installed packages:

```bash
pip list
```

You should see packages such as:

* pytest
* pluggy
* packaging
* Pygments

### 6. Start the application

```bash
python main.py
```

The application will automatically create the SQLite database and the `books` table if they do not already exist.

### 7. Run the automated tests

```bash
pytest
```

### 8. Daily development workflow

When returning to the project on another day:

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the application:

```bash
python main.py
```

or run the test suite:

```bash
pytest
```

### 9. Rebuilding the environment

If you ever need to recreate the virtual environment:

Deactivate it (if active):

```bash
deactivate
```

Delete the existing environment:

```powershell
Remove-Item .venv -Recurse -Force
```

Create a new one:

```bash
python -m venv .venv
```

Activate it again:

```powershell
.venv\Scripts\Activate.ps1
```

Reinstall the dependencies:

```bash
pip install -r requirements.txt
```
