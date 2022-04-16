import json


def load_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidate(candidate):
    return f'''
Имя кандидата - {candidate['name']}
Позиция кандидата - {candidate['position']}
Навыки через запятую - {candidate['skills']}
'''


def get_all_candidates(candidates):
    all_candidates = '<pre>'
    for candidate in candidates:
        all_candidates += get_candidate(candidate)

    return all_candidates + '<pre>'


def get_candidate_by_id(candidates, candidate_id):
    for candidate in candidates:
        if int(candidate_id) == candidate['id']:
            return f'''<img src={candidate['picture']}>

<pre>
Имя кандидата - {candidate['name']}
Позиция кандидата - {candidate['position']}
Навыки через запятую - {candidate['skills']}
</pre>'''


def get_skill_candidates(candidates, skill):
    candidates_with_skill = '<pre>'
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            candidates_with_skill += get_candidate(candidate)
    return candidates_with_skill + '<pre>'
