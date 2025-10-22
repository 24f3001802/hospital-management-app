from flask import Flask
from application.database import db
 
app = None

def create_app():
    app = Flask(__name__) 
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///ecard.sqlite3"#3 database
    db.init_app(app)
    app.app_context().push()#runtime error, brings everything under context of flask application
    return app

app = create_app()
from application.controllers import *

# from application.models import * #indirect connection using controllers.py


if __name__ == "__main__":
    app.run()