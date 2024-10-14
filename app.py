from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sefterli0506@localhost:5432/flasktutorialsdb'


    db.init_app(app)

    from routes import  register_routes
    register_routes(app,db)

    migrate = Migrate(app, db)
    return app