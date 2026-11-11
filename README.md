# Mechatronics quiz app

## Project Overview

Mechatronics Skills Challenge is a beginner-friendly Python quiz application created for Mechatronics Engineering students. It helps students practise important concepts from different areas of mechatronics.

Instead of giving questions from only one general list, the user first chooses a topic. The application then presents five questions from that topic, checks each answer, gives a short learning note, and displays the final result.

## Topics Covered

- Electronics
- Sensors and Actuators
- Automation and PLC
- Mechanical Systems

## Main Features

- Student name entry
- Topic selection before the quiz begins
- Five questions for each selected topic
- Random question order
- Automatic answer checking
- Immediate feedback after each answer
- Short explanation or learning note for every question
- Automatic score and percentage calculation
- Performance remark based on the score
- List of questions the student should revise
- Option to try another topic

## Technologies Used

- Python 3
- `random` module

## Python Concepts Used

- Variables
- Lists and dictionaries
- Functions
- `for` and `while` loops
- `if`, `elif` and `else` statements
- User input and input validation
- Integer and percentage calculations

## How to Run

### Requirement

Python 3 must be installed on your computer or available in a Python app such as Pydroid 3.

### Steps

1. Download or clone this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python mechatronics_skills_challenge.py
```

4. Enter your name.
5. Choose a topic from the menu.
6. Answer the five questions and view your result.

## Sample Output

```text
==========================================
       MECHATRONICS SKILLS CHALLENGE
==========================================
Enter your name: Student

CHOOSE A MECHATRONICS TOPIC
1. Electronics
2. Sensors and Actuators
3. Automation and PLC
4. Mechanical Systems

Enter the number of your chosen topic: 3

Hello Student!
Topic: Automation and PLC
You will answer 5 questions. Good luck!

Question 1 of 5
What is the full meaning of PLC?
A. Power Line Circuit
B. Programmable Logic Controller
C. Program Load Control
D. Process Level Computer
Your answer (A/B/C/D): B
Correct!
Learning note: PLC stands for Programmable Logic Controller.
```

*The question order and the sample question shown may vary because the program shuffles questions.*

## My Own Twist

My own twist is the **topic-based learning system**. The user chooses a mechatronics area before starting, and every question comes with a short learning note. At the end, the program also lists the questions that need more revision.

## What I Learned

Through this project, I practised:

- Organising related questions using dictionaries and lists
- Creating and calling Python functions
- Using loops to repeat questions and menus
- Applying conditions to check answers
- Validating user input
- Using the random module to shuffle questions
- Calculating scores and percentages

## Author

Ajao Oladoye Asamu  
ND II Mechatronics Engineering  
Yaba College of Technology
