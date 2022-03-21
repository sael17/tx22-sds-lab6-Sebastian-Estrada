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

# def checker(capitals):
#     correct_capital = {"NY": "albany", "CA": "sacramento","FL": "tallahassee", "TX": "austin", "NC": "raleigh"}
#     score = {}
#     for state in capitals:
#         if capitals[state].lower() == correct_capital[state]:
#             score[state] = 'Correct'
#         else:
#             score[state] = 'Incorrect. It should be '+correct_capital[state]
#     return score

def verify_answers(students_answers):
    # US States with their correspondant capitals
    state_capitals = correct_capital = {"NY": "albany", "CA": "sacramento","FL": "tallahassee", "TX": "austin", "NC": "raleigh"}
    # Dictionary to return which holds the evaluation (grade of the student)
    student_quiz_result = {}
    # Check how many did questions the student got right
    student_quiz_grade = 0
    for state in correct_capital:
        if students_answers[state].lower() == state_capitals[state]:
            student_quiz_result[state] = "Correct Answer. Great Job!"
        else:
            student_quiz_result[state] = "Incorrect Capital :(. Good Luck Next Time!"
            student_quiz_grade += 1

    return student_quiz_result
  

def calculateQuizScore(student_quiz_answers):
    state_capitals = correct_capital = {"NY": "albany", "CA": "sacramento","FL": "tallahassee", "TX": "austin", "NC": "raleigh"}
  # Check how many did questions the student got right
    student_quiz_grade = 0
    for state in correct_capital:
        if student_quiz_answers[state].lower() == state_capitals[state]:
            student_quiz_grade += 1
            
    return "Your Grade In This Quiz is: " + str(student_quiz_grade) + "/" + str(len(student_quiz_answers)) + " which is equal to " + (str(((student_quiz_grade/len(student_quiz_answers))*100))) + "%"


