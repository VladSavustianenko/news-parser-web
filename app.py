import os

from flask_cors import CORS

from src.db_models import *
# from src.job import start_job

port = int(os.environ.get("PORT", 5000))
# db.init_app(app)


# with app.app_context():
#     db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# start_job()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
