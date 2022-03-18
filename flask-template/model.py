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

def checker(capitals):
    correct_capital = {"NY": "albany", "CA": "sacramento","FL": "tallahassee", "TX": "austin", "NC": "raleigh"}
    score = {}
    for state in capitals:
        if capitals[state].lower() == correct_capital[state]:
            score[state] = 'correct'
        else:
            score[state] = 'incorrect. It should be '+correct_capital[state]
    return score