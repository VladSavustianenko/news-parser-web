import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin' \
#                                                        f'@localhost/news'
print(os.getenv("DATABASE_URL"))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'

CORS(app)
