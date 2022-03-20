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
from flask import Flask
from flask import render_template
from flask import request
from model import checker

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results',methods=['GET','POST'])
def check():
    if request.method == "GET":
        return "Please fill the form before hand."

    else:
        answers = {"NY": request.form['New York'], "CA": request.form['California'], "FL": request.form['Florida'],"TX":request.form['Texas'],"NC":request.form['Norh Carolina']}
        score = checker(answers)
        return render_template('results.html',score=score, answers = answers)
