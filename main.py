from utils import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    list_candidates = '<br>'
    for candidate in load_candidates():
        position = candidate["position"]
        list_candidates += str(position) + '<br>' # тоже что '\n'
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
    results += candidate["name"] + '<br>'
    results += str(candidate["position"]) + '<br>'  # тоже что <br>
    results += candidate["skills"] + '<br>'

    return f'''
           <img src="{candidate['picture']}">
           <pre> {results} </pre>
           '''


@app.route("/candidate/<skill>")
def get_candidate_by_skills(skill):
    candidates = get_by_skill(skill)
    if not candidates:
         return "Кандидат с такими навыками не найден"

    results = "<br>"
    for candidate in candidates:
        results += f'''
                <img src="{candidate['picture']}">
                <br>
                '''

        results += candidate["name"] + '<br>'
        results += str(candidate["position"]) + '<br>'
        results += candidate["skills"] + '<br>'

    return results

app.run()