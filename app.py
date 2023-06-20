from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from helper import generate_questions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class QuestionForm(FlaskForm):
    pass

@app.route('/renderForm', methods=['GET', 'POST'])
def form_generator():
    questions = []

    with open("questions.txt", "r") as file:
        for line in file:
            # Remove the line break at the end of each line
            item = line.strip()
            questions.append(item)

    for idx, question in enumerate(questions):
        setattr(QuestionForm, f'question_{idx}', StringField(question))

    setattr(QuestionForm, 'submit', SubmitField('Submit'))

    form = QuestionForm()
    if form.validate_on_submit():
        # Process the form data
        answers = []
        for idx, _ in enumerate(questions):
            answer = getattr(form, f'question_{idx}').data
            answers.append(answer)
        # Perform desired actions with the form data
        print("Answers:", answers)
        # Optionally, redirect to another page or display a success message
        return 'Form submitted successfully!'
    return render_template('form.html', form=form)

@app.route('/', methods=['GET'])
def render_home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_output():
    data = request.get_json()
    user_input = data.get('input')
    if user_input == '':
        user_input = 'general health diagnosis'
    questions = generate_questions(descroption=user_input)

    print("Here are questions", questions)

    with open("questions.txt", "w") as file:
        for item in questions:
            file.write(item + "\n")

    return jsonify({k:v for k,v in enumerate(questions)})

if __name__ == '__main__':
    app.run(debug=True)

