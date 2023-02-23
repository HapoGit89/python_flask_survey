from flask import Flask, request, render_template, redirect


from surveys import *

app = Flask(__name__)

responses = []

@app.route('/')
def show_start():
    title = personality_quiz.title
    inst = personality_quiz.instructions
    return render_template('start.html', survey_title=title, instructions=inst)


@app.route('/questions/<question_number>')
def show_question(question_number):
    if int(question_number) < len(personality_quiz.questions):
        number = int(question_number)
        questiontext = personality_quiz.questions[number].question
        answers = personality_quiz.questions[number].choices
        return render_template('questions.html', question = questiontext, question_number= number, answers= answers)
    else:

        return "End!"

@app.route('/answers/<answer_number>', methods= ['POST'])
def save_and_redirect(answer_number):
    answer = request.form['answer']
    num = int(answer_number)
    responses.append(answer)
    print(responses)
    return redirect(f"/questions/{num+1}")