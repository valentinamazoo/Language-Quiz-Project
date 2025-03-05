# Language-Quiz-Project
# Spanish-to-English Translation Quiz

Project Overview
This project is a Flask-based web application designed to quiz users on Spanish-to-English translations. It presents users with Spanish words and asks them to provide their English equivalents. Results are displayed at the end.

Structure & Purpose
- Home Page: Welcomes users and links to the quiz.
- Quiz Page: Users fill in their translations for the given Spanish words.
- Results Page: Displays the score and offers a retry option.

How to Run
1. **Install Flask**:
2. **Run the Application**:
3. **Access the App**: Open your browser at `http://127.0.0.1:5000/`.

File Structure
- project.py: Core logic of the app (Flask routes and quiz handling).
- templates/index.html: Home page (introduction).
- templates/quiz.html: Quiz form where users input translations.
- templates/result.html: Results page showing the user's score

Key Functions
- index(): Renders the homepage.
- quiz(): Processes the user's quiz input and computes the score.
- result(score): Displays the user's final score after completing the quiz.

Key Technologies
- Flask: Web framework to handle routing and logic.
- HTML: Used for rendering the pages (home, quiz, results).

Chi do Takeaway
- Clarity: Clear user experience with direct feedback.
- Modularity: Separated logic and design for scalability.
- Interaction: Simple user input handled dynamically.





