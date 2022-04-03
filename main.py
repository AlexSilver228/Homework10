import flask

import utils

app = flask.Flask(__name__)

candidates = utils.users_info()


@app.route("/")
def page_index():
    str_candi = "<pre>"
    for candidate in candidates.values():
        str_candi += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candi += "<pre>"
    return str_candi


@app.route("/candidate/<int:id>")
def page_candidate(id):
    candidate = candidates[id]
    str_candi = f"<img src={candidate['picture']}> <br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']} <br><br>"
    return str_candi


@app.route("/skills/<skill>")
def candidate_skills(skill):
    candidate_skill = "<pre>"
    for candidate in candidates.values():
        skills_ = candidate["skills"].split(", ")
        skills_ = [i.lower() for i in skills_]
        if skill in skills_:
            candidate_skill += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    candidate_skill += "</pre>"
    return candidate_skill


app.run(debug=True)
