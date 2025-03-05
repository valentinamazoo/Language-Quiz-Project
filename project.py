from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

translations = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "agua": "water",
    "comida": "food",
    "libro": "book"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    if request.method == 'POST':
        score = 0
        for spanish_word, english_translation in translations.items():
            user_answer = request.form.get(spanish_word, "").strip().lower()
            if user_answer == english_translation:
                score += 1
        return redirect(url_for('result', score=score))
    return render_template('quiz.html', translations=translations)

@app.route('/result/<int:score>')
def result(score):
    total_questions = len(translations)
    return render_template('result.html', score=score, total=total_questions)

if __name__ == "__main__":
    app.run(debug=True)