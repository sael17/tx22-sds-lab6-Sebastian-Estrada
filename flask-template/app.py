# Sebastian Estrada
# Ujjwal Adhikari


# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from multiprocessing.connection import answer_challenge
from flask import Flask
from flask import render_template
from flask import request
from model import verify_answers
from model import calculateQuizScore

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/results", methods=["GET","POST"])
def quiz_validification():
    # Student has not filled the quiz
    if request.method == "GET":
        return "Please Fill Out The Quiz Before Hand"
    else:
        # Dictionary that contains the student's answers 
        student_answers = {"NY": request.form['New York'], "CA": request.form['California'], "FL": request.form['Florida'],"TX":request.form['Texas'],"NC":request.form['Norh Carolina']}
        student_quiz_score = verify_answers(student_answers)
        student_grade = calculateQuizScore(student_answers)
        return render_template("results.html", student_quiz_score=student_quiz_score,student_answers=student_answers,student_grade=student_grade)

