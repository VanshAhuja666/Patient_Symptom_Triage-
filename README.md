# Patient_Symptom_Triage-
A basic Python project that takes patient symptoms and vital signs, applies simple rule-based logic to identify the affected body system, and classifies the case as urgent, moderate, or mild. Designed for health informatics learning using only core Python concepts.
# Patient Symptom Triage System
## Overview
This is a console-based Python project that accepts basic patient details like symptoms 
and vital signs and classifies the condition as Urgent, Moderate, or Mild using 
rule-based logic. It also identifies the main affected system and suggests a department.

This project is developed using only basic Python concepts without using any AI, GUI, 
or external libraries.

## Features
- Takes patient symptoms and vital signs as input.
- Applies rule-based decision logic.
- Classifies patient condition into three levels.
- Identifies body system affected.
- Gives health advice for each case.
- Modular Python file structure.

## Technologies Used
- Python
- Basic Console Input/Output

## Modules Used
- triage_input.py
- triage_rules.py
- triage_engine.py
- triage_advice.py
- main.py

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python is installed on your system.
3. Open terminal or command prompt.
4. Navigate to the project folder.
5. Run the program using: python main.py
6. Or Open Jupyter Notebook on your system.
7. Go to the folder where you have downloaded or cloned this project.
8. Make sure all these files are in the same folder:
      main.py,
      triage_input.py,
      triage_engine.py,
      triage_rules.py,
      triage_advice.py,
      Main_PythonFile.ipynb
9. Open the File :- Main_PythonFile.ipynb
10. And You Can Directly Run the Pre-Written First Cell inside Main_PythonFile.ipynb Or
11. In a new cell, write this code :- %run main.py
12. Press Shift + Enter to run the cell.
13. The program will start running inside the notebook, and you can enter patient details as Adressed Below.
14. Important Note :-
Make sure all .py files and the .ipynb file are inside the same directory, otherwise Python will not be able to import the modules.

## How to Use

- Enter patient details as asked by the program.
- Choose symptoms from the displayed list.
- Enter temperature, BP and SpO2 values.
- The system will display risk category and advice.

## Sample Output

Input:  
Symptoms: chest pain, dizziness  
SpO2: 86  
BP: 150/95  

Output:  
Category: URGENT  
System: Cardiac  
Department: Cardiology  

## Authors

Developed by: Vansh Ahuja  
Course: B.Tech CSE (Health Informatics)  
University: VIT Bhopal
