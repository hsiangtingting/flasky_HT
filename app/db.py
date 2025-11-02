from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
from .models.base import Base

db = SQLAlchemy(model_class=Base)


