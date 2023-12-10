import requests

from src.db_models import Topic, db, Content, TopicLog, app
from src.model import TOPICS, TopicModel, ContentModel


class Parser:
    _URL = 'https://www.washingtonpost.com/prism/api/prism-query'

    _OFFSET_FIRST_INIT_VALUES = [0, 50, 100, 150]
    _OFFSET_VALUES = [0]
    _LIMIT = 50

    def _get_offset_values(self):
        if self._is_first_init():
            return self._OFFSET_FIRST_INIT_VALUES

        return self._OFFSET_VALUES

    def _is_first_init(self):
        return not Topic.query.filter_by(id=1).first()

    def _is_already_exist(self, id):
        return Topic.query.filter_by(source_id=id).first()

    def _fetch(self, query, section, subsection, offset):
        params = {
            '_website': 'washpost',
            'query': '{"query": "prism://prism.query' + query + '&offset=' + str(offset) + '&limit=' + str(self._LIMIT) + '"}'
        }

        # try:
        resp = requests.get(self._URL, params)
        json_data = resp.json()
        items = json_data['items']

        # repeats = 0
        for item in items:
            if not self._is_already_exist(item['_id']):
                repeats = 0
                topic_model = TopicModel()

                topic_model.section = section
                topic_model.subsection = subsection

                topic_model.source_id = item['_id']
                topic_model.type = item['type']

                if 'tracking' in item and 'author_name' in item['tracking']:
                    topic_model.author = item['tracking']['author_name']

                if 'headlines' in item and 'basic' in item['headlines']:
                    topic_model.headline = item['headlines']['basic']

                if 'website_url' in item:
                    topic_model.website_url = item['website_url']

                if 'fusion_additions' in item and 'teaser' in item['fusion_additions']:
                    topic_model.teaser = item['fusion_additions']['teaser']

                if 'fusion_additions' in item and 'promo_image' in item['fusion_additions'] and 'url' in item['fusion_additions']['promo_image']:
                    topic_model.promo_image = item['fusion_additions']['promo_image']['url']

                if 'first_publish_date' in item:
                    topic_model.publish_date = item['first_publish_date']

                if 'description' in item and 'basic' in item['description']:
                    topic_model.description = item['description']['basic']

                new_topic = Topic(topic_model)

                db.session.add(new_topic)
                db.session.commit()
                print('Add topic id:', new_topic.source_id, ' --- ', new_topic.headline.encode("utf-8"))

                if 'content_elements' in item and len(item['content_elements']):
                    content_model = ContentModel()
                    content_model.topic_id = new_topic.id
                    content_model.content = ''

                    for elem in item['content_elements']:
                        if 'content' in elem and '_id' in elem:
                            content_model.content += elem['content']

                    db.session.add(Content(content_model))
                    db.session.commit()

                new_topic_log = TopicLog(new_topic.id)

                db.session.add(new_topic_log)
                db.session.commit()
            else:
                print(item['_id'], 'Already exist')
                # repeats += 1

                # if repeats == 5:
                #     print('\nBREAK DUE TO 5 REPEATS\n')
                #
                #     return
        # except:
        #     print('\nCOULD NOT FETCH DATA', params)
        #     return

    def execute(self):
        with app.app_context():
            offset_values = self._get_offset_values()

            for topic in TOPICS:
                for offset in offset_values:
                    print('\n----------------------------------\n')
                    print('OFFSET', offset, '\n', topic)
                    if topic['children']:

                        for sub in topic['children']:
                            print('\n', sub['title'], '\n')
                            self._fetch(sub['query'], topic['title'], sub['title'], offset)

                    else:
                        print('\n', topic['title'], '\n')
                        self._fetch(topic['query'], topic['title'], None, offset)
