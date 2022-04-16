import json
from flask import Flask
from pprint import pprint as pp
from utils import load_json_file, get_all_candidates, get_candidate_by_id, get_skill_candidates

app = Flask(__name__)

@app.route('/')
def main_page():
    candidates = load_json_file('candidates.json')
    return get_all_candidates(candidates)


@app.route('/candidates/<candidate_id>')
def candidates_page(candidate_id):
    candidates = load_json_file('candidates.json')
    return get_candidate_by_id(candidates, candidate_id)


@app.route('/skills/<skill>')
def skill_page(skill):
    candidates = load_json_file('candidates.json')
    return get_skill_candidates(candidates, skill)


app.run()
