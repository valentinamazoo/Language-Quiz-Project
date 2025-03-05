# Language-Quiz-Project
# Spanish-to-English Translation Quiz

#### Video Demo:  https://youtu.be/bSLxb6_TGCo

#### Description:
The *Spanish-to-English Translation Quiz* is a fun and interactive web-based quiz application built using the *Flask* framework. The purpose of this project is to help users practice their Spanish-to-English translation skills in an engaging and simple manner. The application generates a quiz with a set of Spanish words, and users must provide the correct English translation for each word. Upon completing the quiz, users receive feedback on their answers and their total score.

This project was created to provide a lightweight, interactive web app that allows users to test and improve their knowledge of Spanish vocabulary in a fun and easy way. The interface is clean and user-friendly, ensuring a smooth experience from start to finish. The quiz is dynamic, with the Spanish words changing each time the user reloads or revisits the quiz page, keeping the challenge fresh.



### Project Overview:
This project is a *Flask-based web application* designed to quiz users on Spanish-to-English translations. It presents users with Spanish words and asks them to provide their English equivalents. Results are displayed at the end.


### Structure & Purpose:
•⁠  ⁠*Home Page*: Welcomes users and provides a link to start the quiz.
•⁠  ⁠*Quiz Page*: Users fill in their translations for the given Spanish words. They receive immediate feedback for each word.
•⁠  ⁠*Results Page*: Displays the user’s score at the end of the quiz and offers a retry option.


### Key Features:
•⁠  ⁠*Dynamic Quiz*: Randomized questions from a fixed list of translations, ensuring variety each time the quiz is played.
•⁠  ⁠*Instant Feedback*: Users are given immediate feedback on whether their answers are correct or incorrect.
•⁠  ⁠*Results Display*: At the end of the quiz, the user is shown their score and can retry the quiz.


### How to Run the Project:
 ⁠*Clone the Repository*: 
   To begin, clone the repository to your local machine using the following command:
   ```bash
   git clone <your-github-repo-url>
Install Flask: If you haven’t already, install Flask by running the following command:
pip install Flask

Run the Application: To run the application, execute the following command:
python project.py

Access the App: Once the app is running, open your browser and navigate to:
http://127.0.0.1:5000/

Play the Quiz:
Start the quiz by clicking the link on the home page.
Translate the Spanish words into English as they appear.
After finishing, check your results and try again if you'd like to improve your score!

File Structure:
project.py: The core logic of the app. It handles the Flask routes and quiz functionality.
templates/index.html: Home page that introduces the quiz and provides a link to start it.
templates/quiz.html: Displays the quiz form where users input their translations.
templates/result.html: Displays the user’s score after completing the quiz.

Key Functions:
index(): Renders the homepage where users can start the quiz.
quiz(): Processes the user's quiz input, checks the answers, and computes the total score.
result(score): Displays the final score after the quiz is completed and offers the option to try again.

Key Technologies:
Flask: A lightweight web framework used to handle routing and server-side logic.
HTML: Used to structure the pages for the home page, quiz, and results.
CSS: Simple styling to enhance the user experience.

Design Considerations:
Clarity: The user interface is clear and easy to navigate, ensuring a straightforward experience from beginning to end.
Modularity: The app structure separates the logic (project.py) from the design (HTML files) for better scalability and future enhancements.
Interaction: The quiz is dynamic, with real-time input processing that provides immediate feedback on user responses.

Future Enhancements:
While the current project version is focused on a simple quiz with basic features, there are many possibilities for future improvements:
User Authentication: Allow users to sign up and track their quiz scores over time.
Database Integration: Store quiz data and user progress in a database to allow for more complex features like personalized quiz questions.
Mobile Responsiveness: Adapt the app for better use on mobile devices.
Multiple Languages: Expand the quiz to support translations between other languages.

Acknowledgements:
Flask: For being an easy-to-use and powerful web framework.
HTML & CSS: For helping us create a simple yet effective interface.





