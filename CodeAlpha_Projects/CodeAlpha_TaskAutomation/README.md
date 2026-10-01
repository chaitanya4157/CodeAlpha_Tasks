CodeAlpha Task Automation

1. Project Overview

The Task Automation project is a Python-based program that automatically organizes JPG files in a folder.

Instead of manually searching for JPG files and moving them one by one, the program checks the files in a selected folder and moves all JPG files into a separate folder named `JPG_Files`.

This project demonstrates how Python can be used to automate a simple repetitive task.

2. Key Features

- Takes a folder path from the user
- Checks whether the folder exists
- Creates a separate `JPG_Files` folder
- Finds JPG files automatically
- Moves JPG files into the new folder
- Counts the number of files moved
- Displays the result to the user

3. Python Concepts Used

- `os` module
- `shutil` module
- Variables
- Conditional statements
- `for` loop
- User input
- File and folder handling
- String methods

4. Project Structure


CodeAlpha_TaskAutomation
├── task_automation.py
└── README.md


5. How to Run

1. Open the project folder in VS Code.
2. Open `task_automation.py`.
3. Run the program using Python.
4. Enter the path of the folder containing the JPG files.

python task_automation.py


6. How the Program Works

The program first asks the user to enter a folder path.

It checks whether the folder exists. If the folder is found, the program creates a folder named `JPG_Files`.

The program then checks the files inside the selected folder one by one.

If a file ends with `.jpg`, it is moved into the `JPG_Files` folder.

Finally, the program displays the total number of JPG files that were moved.


7. Design Approach

The `os` module is used to work with folders and file paths.

The `shutil` module is used to move JPG files from the original folder to the new folder.

A `for` loop checks each file, while an `if` condition identifies JPG files.

A counter is used to keep track of the number of files moved.

8. What I Learned

Through this project, I learned how Python can be used to automate file organization.

I practiced working with folders and files using the `os` module and moving files using the `shutil` module.

I also learned how loops and conditions can be combined to automate repetitive tasks.

9. Future Improvements

Possible future improvements include:

- Organizing different file types into separate folders
- Supporting `.jpg` and other image formats
- Allowing the user to choose the file type
- Organizing files based on their extensions

10. Internship Context

This project was developed as part of the CodeAlpha Python Programming Internship.

The project follows the Task Automation requirement of automating a small repetitive task using Python.

11. Author

Chaitanya Deshaboina