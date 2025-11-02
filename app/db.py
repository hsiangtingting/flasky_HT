from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
from .models.base import Base

db = SQLAlchemy(model_class=Base)


from flask_migrate import Migrate
from .models.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
