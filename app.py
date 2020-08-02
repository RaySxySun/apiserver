import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#     user=os.environ['POSTGRES_USER'], pw=os.environ['POSTGRES_PW'], url=os.environ['POSTGRES_URL'], db=os.environ['POSTGRES_DB'])
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
print(os.environ['APP_SETTINGS'])

from models import Result


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
