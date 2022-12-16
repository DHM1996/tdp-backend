from db.dao import user as user_dao
from schema.profile import ProfileSchema
from db.model.users import User
from utils.validator import validate_user, validate_profession


def update_profile(profile: ProfileSchema):
    validate_user(profile.user_id)
    validate_profession(profile.profession_id)
    user_dao.update_profile(profile)
    return {"message": "user profile updated successfully"}


def get_profile(user_id):
    db_user: User = validate_user(user_id)
    profile = ProfileSchema(
                            user_id=db_user.id,
                            name=db_user.name,
                            surname=db_user.surname,
                            link_pic=db_user.link_pic,
                            longitude=db_user.longitude,
                            latitude=db_user.latitude,
                            profession_id=db_user.profession_id
                            )
    return profile
