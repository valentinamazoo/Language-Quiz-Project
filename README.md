# Language-Quiz-Project
Spanish-to-English Translation Quiz

Video Demo: [Insert Video URL here

Description:
This project is a simple Spanish-to-English Translation Quiz implemented in Python. The goal of this program is to quiz the user by providing Spanish words and asking them to translate them into English. At the end of the quiz, the program gives the user a score based on how many correct answers they provided.

This project demonstrates how to use dictionaries, loops, and conditional statements in Python to create an interactive quiz. It also showcases the importance of testing functions, with unit tests written using pytest to ensure the functionality of the quiz works correctly.

Project Structure:
The project contains two files:

project.py - The main Python file that contains the code for the quiz.
test_project.py - The file that contains unit tests for some of the functions in project.py.
How to Run the Project:

Requirements:
Make sure you have Python installed on your computer.

To run the project, follow these steps:

Clone the repository:
git clone https://github.com/valentinamazoo/Language-Quiz-Project.git
cd Language-Quiz-Project
Run the quiz: Run the following command in your terminal to start the quiz:
python project.py
The program will prompt you with Spanish words and ask for their English translation. After completing all the questions, you’ll receive your score.
Run the unit tests: To ensure the functions are working correctly, you can run the unit tests using pytest:
pytest test_project.py
Make sure you have pytest installed. If not, install it using:
pip install pytest

Functions in project.py:

main()
Purpose: This is the main function that starts the quiz. It calls the language_quiz() function, which handles the quiz logic.
How it works: It prints a welcome message, displays instructions, and manages the flow of the quiz. After the quiz is completed, it outputs the final score.
language_quiz()
Purpose: This function runs the quiz by iterating through a predefined dictionary of Spanish-to-English word pairs.
How it works: It uses a for loop to ask the user for translations of Spanish words and checks the users input against the correct English translation. The user's score is updated for each correct answer, and after all questions are answered, the total score is displayed.
translate_word(spanish_word)
Purpose: This function takes a Spanish word as input and returns its corresponding English translation from the dictionary.
How it works: It uses the translations dictionary to look up the English equivalent of the given Spanish word. If the word is not found, it returns a message indicating that the translation is unavailable.
check_translation(user_answer, correct_answer)
Purpose: This function checks if the user’s answer matches the correct English translation.
How it works: It compares the user’s input (converted to lowercase) with the correct answer. If they match, it returns True; otherwise, it returns False.
Functions in test_project.py:

test_translate_word()
Purpose: This is a test for the translate_word() function.
How it works: It checks if the translate_word() function correctly returns the expected English translations for given Spanish words. It also tests for words that don’t exist in the dictionary.
test_check_translation()
Purpose: This is a test for the check_translation() function.
How it works: It tests if the function correctly identifies whether the user's input matches the correct English translation.
Design Choices:

Translations Dictionary: The program uses a dictionary where the keys are Spanish words and the values are their corresponding English translations. This allows easy lookup and management of the word pairs.
Lowercase Input: All user inputs are converted to lowercase to ensure the comparison is case insensitive, making it more user friendly.
Test Coverage: Unit tests are implemented for key functions to ensure the program behaves as expected in different scenarios.
