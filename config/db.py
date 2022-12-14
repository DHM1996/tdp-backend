from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
import os
import model

# You should set this environment variables before running the application
db_host = os.getenv("db_host")
db_port = os.getenv("db_port")
db_database = os.getenv("db_database")
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")

try:
    engine = create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            db_username, db_password, db_host, db_port, db_database
        ))

    # Create session and model if necessary
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    model.Base.query = db_session.query_property()
    model.Base.metadata.create_all(bind=engine)

except Exception as err:
    raise Exception("Unable to connect to DB, check your environment variables")


def get_db():
    return db_session
