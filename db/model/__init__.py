from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata_obj = MetaData()
Base = declarative_base(metadata_obj)
