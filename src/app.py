from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin' \
#                                                        f'@localhost/news'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vezxqcorwfukqk:a5992eddeaeec73a3030c38c124e21f84b725391fab70658e2a444377c132640@ec2-18-202-8-133.eu-west-1.compute.amazonaws.com:5432/dfqcc1kqh52rno'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'

CORS(app)
