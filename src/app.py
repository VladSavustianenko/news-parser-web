import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin' \
#                                                        f'@localhost/news'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'

CORS(app)
