from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from src.app import app
from src.model import TopicModel, ContentModel

db = SQLAlchemy(app)


class Topic(db.Model):
    __tablename__ = 'Topic'

    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String)
    author = db.Column(db.String)
    headline = db.Column(db.String)
    website_url = db.Column(db.String)
    teaser = db.Column(db.String)
    promo_image = db.Column(db.String)
    publish_date = db.Column(db.DateTime)
    description = db.Column(db.String)
    section = db.Column(db.String)
    subsection = db.Column(db.String)

    def __init__(self, topicModel: TopicModel):
        self.source_id = topicModel.source_id
        self.type = topicModel.type
        self.author = topicModel.author
        self.headline = topicModel.headline
        self.website_url = topicModel.website_url
        self.teaser = topicModel.teaser
        self.promo_image = topicModel.promo_image
        self.publish_date = topicModel.publish_date
        self.description = topicModel.description
        self.section = topicModel.section
        self.subsection = topicModel.subsection


class Content(db.Model):
    __tablename__ = 'Content'

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('Topic.id'), nullable=False)
    source_id = db.Column(db.String)
    content = db.Column(db.String)
    order = db.Column(db.Integer)

    def __init__(self, content_model: ContentModel):
        self.topic_id = content_model.topic_id
        self.source_id = content_model.source_id
        self.content = content_model.content
        self.order = content_model.order


class TopicLog(db.Model):
    __tablename__ = 'Topic_logs'

    id = db.Column(db.Integer, db.ForeignKey('Topic.id'), primary_key=True)
    added_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id):
        self.id = id
