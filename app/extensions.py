from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#from flask_restful import Resource, Api


db = SQLAlchemy()
migrate = Migrate()
