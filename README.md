# 🗺 U.S. States Quiz 🏆🗺️

A fun and educational `Python` quiz game built with `turtle graphics` and `pandas`.
Test your knowledge of U.S. geography by naming all 50 states!

When you guess correctly, the state’s name will appear on the U.S. map.
If you type `"Exit"`, the game ends and automatically creates a `CSV file` containing the states you didn’t guess — perfect for studying and improving your knowledge later.

## 🧩 Features

- Interactive U.S. map using Python’s turtle graphics

- Real-time input for guessing state names

- Correct answers are displayed directly on the map at the state’s coordinates

- Progress tracking: see how many states you’ve correctly identified

- Exit anytime using "Exit" command

- Learning mode: generates a `states_to_learn.csv` file with all unguessed states for further study

## 🖼️ Preview
![Preview - U.S. States Quiz](./images/preview.png)

## 🛠️ Technologies Used

- Python 3

- turtle (for graphical interface and map display)

- pandas (for data handling and CSV export)

## 📁 Project Structure

- 📦 **us-states-quiz-game/**
  - 📂 **data/**
    - `50_states.csv` — List of all 50 U.S. states with coordinates (state, x, y)
    - `states_to_learn.csv` — Generated after quitting; contains unguessed states
  - 📂 **images/**
    - `blank_states_img.gif` — Map of the U.S. used for the quiz background
  - `main.py` — Main game script
  - `README.md` — This file

## ▶️ How to Play

1) Run the script:
`python main.py`
A window will open showing the map of the U.S.

2) Type a state name in the input box and press Enter. 
If correct, the name will appear on the map. 
If incorrect, try again!

3) Type Exit at any time to quit the game. 
After exiting, a file called states_to_learn.csv will be generated containing the states you missed.

📘 Example Output:
- state,x,y
- Alabama,139,-77
- Alaska,-204,-170
...

## 🎯 Learning Purpose

This quiz is a great way to learn and memorize all 50 U.S. states interactively.
You can repeatedly play the game using the states_to_learn.csv file to focus on the states you haven’t mastered yet.