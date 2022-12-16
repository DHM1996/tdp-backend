import db.dao.professions as professions_dao


def get_professions(profession_id):
    if profession_id:
        result = professions_dao.get_profession_by_id(profession_id)
    else:
        result = professions_dao.get_professions()
    return result
