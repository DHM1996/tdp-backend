from fastapi import HTTPException

from validator.validator import validate_professionals_filters, validate_professional
from math import sqrt
import db.dao.professionals as professionals_dao


def get_professionals(professional_id, profession_id, user_longitude, user_latitude, dist):
    validate_professionals_filters(professional_id, profession_id, user_longitude, user_latitude, dist)

    if professional_id:
        return {
            "professionals": [validate_professional(professional_id)],
            "message": "As you specify professional_id, other filters are ignored"
        }

    professionals = professionals_dao.get_professionals(profession_id)

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
