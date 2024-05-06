import os

from src.db_models import *
from src.job import start_job

port = int(os.environ.get("PORT", 5000))
db.init_app(app)


with app.app_context():
    db.create_all()


start_job()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
