from flask import Flask, request, render_template, redirect, flash


from surveys import *

app = Flask(__name__)

app.secret_key = "super secret key"

responses = []

@app.route('/')
def show_start():
    title = personality_quiz.title
    inst = personality_quiz.instructions
    return render_template('start.html', survey_title=title, instructions=inst)


@app.route('/questions/<question_number>')
def show_question(question_number):
    number = int(question_number)
    if number != check_question_val(int(question_number)):
        print("before flash")
        flash ("Please answer the questions in chronological order!")
        print("after flash")
        return redirect(f"/questions/{check_question_val(int(question_number))}")
    
    if int(number) < len(personality_quiz.questions):
        questiontext = personality_quiz.questions[number].question
        answers = personality_quiz.questions[number].choices
        return render_template('questions.html', question = questiontext, question_number= number, answers= answers)
    else:

        return render_template('thanks.html')

@app.route('/answers/<answer_number>', methods= ['POST'])
def save_and_redirect(answer_number):
    answer = request.form['answer']
    num = int(answer_number)
    responses.append(answer)
    print(responses)
    return redirect(f"/questions/{num+1}")


def check_question_val(number):
    if number != len(responses):
        return len(responses)
    else:
        return number
