# Notes App

A simple command-line notes application built with **Python**.

The app provides a straightforward way to create and view notes, with all notes stored locally in a text file.

## Features

* Add new notes
* View saved notes
* Automatically save notes to a local file
* Displays a message when no notes are available
* Simple command-line interface
* Lightweight and beginner-friendly

## Tech Stack

* **Python**
* **File Handling**
* **Command-Line Interface**

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/notes-app.git
cd notes-app
```

### 2. Run the application

```bash
python "Notes App.py"
```

The application will open in the terminal and display the available options.

## Usage

When the application starts, you will see:

```text
1. Add note
2. View notes
3. Exit
```

### Add a Note

Select `1` and enter your note.

The note will be saved to `notes.txt`.

### View Notes

Select `2` to display all previously saved notes.

If no notes have been saved yet, the application will display:

```text
No notes available.
```

### Exit

Select `3` to close the application.

## How It Works

The application runs inside a continuous loop and displays the main menu until the user chooses to exit.

When a note is added, the program opens `notes.txt` in append mode and writes the note on a new line.

When viewing notes, the application reads the contents of `notes.txt` and displays them. If the file is empty, it reports that there are no notes available.

## Project Structure

```text
Notes-App/
│
├── Notes App.py
├── notes.txt
└── README.md
```

> `notes.txt` is created/used by the application to store notes locally.

**Completed - Basic Version**

The current version includes the core functionality required for creating, storing, and viewing notes.

## Contributing

Contributions and improvements are welcome.

If you find a bug or have an idea for a feature, feel free to open an issue or submit a pull request.

**Notes App**
A simple Python project for creating and managing local notes.
