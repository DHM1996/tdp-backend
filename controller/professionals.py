from fastapi import HTTPException

from validator.validator import validate_distance_filters, validate_professional
from math import sqrt
import db.dao.professionals as professionals_dao


def get_professionals(professional_id, professional_name, profession_id, user_longitude, user_latitude, dist):
    if professional_id:
        return {
            "professionals": professionals_dao.get_professional_by_id(professional_id),
            "message": "As you specify professional_id, other filters are ignored"
        }

    if professional_name:
        return {
            "professionals": professionals_dao.get_professional_by_name(professional_name, profession_id),
            "message": "As you specify professional_name, other filters are ignored except profession"
        }

    validate_distance_filters(user_longitude, user_latitude, dist)
    professionals = professionals_dao.get_professionals_by_profession(profession_id)

    if not user_longitude and not user_latitude and not dist:
        return {
            "professionals": professionals,
            "message": "No filters where included"
        }

    result = []

    for professional in professionals:
        professional_dist = sqrt(
            (float(professional.longitude) - float(user_longitude)) ** 2 + (
                    float(professional.latitude) - float(user_latitude)) ** 2
        )

        if professional_dist <= float(dist):
            result.append(professional)

    return {
        "professionals": professionals,
        "message": "Distance was used"
    }