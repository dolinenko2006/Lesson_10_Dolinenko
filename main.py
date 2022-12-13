from utils import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    list_candidates = '<br>'
    for candidate in load_candidates():
        pk = candidate["pk"]
        list_candidates += str(pk) + '<br>' # тоже что '\n'
        name = candidate["name"]
        list_candidates += name + '<br>'
        skills = candidate["skills"]
        list_candidates += skills + '<br>'


    return f"<pre>{list_candidates}</pre>"


@app.route("/candidate/<int:pk>")
def get_candidates(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return "Кандидат не найден"

    results = '<br>'
    results += str(candidate["pk"]) + '<br>'  # тоже что <br>
    results += candidate["name"] + '<br>'
    results += candidate["skills"] + '<br>'

    return f'<pre> {results} </pre>'


@app.route("/candidate/<skill>")
def get_candidate_by_skills(skill):
    candidates = get_by_skill(skill)
    if not candidates:
         return "Кандидат с такими навыками не найден"

    results = "<br>"
    for candidate in candidates:
        results += str(candidate["pk"]) + '<br>'
        results += candidate["name"] + '<br>'
        results += candidate["skills"] + '<br>'

    return f"{results}"

app.run()