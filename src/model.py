WP_URL = 'https://www.washingtonpost.com/'


class TopicModel:
    source_id = None
    author = None
    headline = None
    website_url = None
    teaser = None
    promo_image = None
    publish_date = None
    description = None
    section = None
    subsection = None


class ContentModel:
    topic_id = None
    content = None


TOPICS = [
    {
        'title': 'politics',
        'children': [
            {
                'title': 'courts-law',
                'query': '/site,/politics/courts-law',
            },
            {
                'title': 'the-202-newsletters',
                'query': '/site,/politics/powerpost',
            },
            {
                'title': 'polling',
                'query': '/polling-page',
            },
            {
                'title': 'white-house',
                'query': '/site,/politics/white-house',
            },
            {
                'title': 'the-fix',
                'query': '/site,/politics/the-fix',
            },
        ],
    },
    {
        'title': 'opinions',
        'children': [
            {
                'title': 'guest-opinions',
                'query': '/guest-opinions',
            },
            {
                'title': 'the-posts-view',
                'query': '/author-english-only,the-posts-view',
            },
            {
                'title': 'global-opinions',
                'query': '/global-opinions-english-only',
            },
            {
                'title': 'local-opinions',
                'query': '/site-and-tag,/opinions,local',
            },
            {
                'title': 'letters-to-the-editor',
                'query': '/letters-to-the-editor/',
            },
        ],
    },
    {
        'title': 'global-opinions',
        'children': None,
        'query': '/global-opinions-english-only',
    },
    {
        'title': 'style',
        'children': [
            {
                'title': 'fashion',
                'query': '/two-sites,/style/fashion,/lifestyle/fashion/',
            },
            {
                'title': 'media',
                'query': '/site,/style/media',
            },
            {
                'title': 'of-interest',
                'query': '/site,/style/of-interest',
            },
            {
                'title': 'power',
                'query': '/site,/style/power',
            },
        ],
    },
    {
        'title': 'climate-environment',
        'children': [
            {
                'title': 'climate-lab',
                'query': '/site,/climate-environment/climate-lab',
            },
            {
                'title': 'environment',
                'query': '/site,/climate-environment/environment',
            },
            {
                'title': 'green-living',
                'query': '/site,/climate-environment/green-living',
            },
            {
                'title': 'business-of-climate',
                'query': '/site,/climate-environment/business-of-climate',
            },
        ],
    },
    {
        'title': 'weather',
        'children': [
            {
                'title': 'extreme-weather',
                'query': '/site,/climate-environment/extreme-weather',
            },
        ],
    },
    {
        'title': 'wellbeing',
        'children': [
            {
                'title': 'food-nutrition',
                'query': '/tag,wb-food',
            },
            {
                'title': 'fitness',
                'query': '/tag,wb-fitness',
            },
            {
                'title': 'mind',
                'query': '/tag,wb-mind',
            },
            {
                'title': 'body',
                'query': '/tag,wb-body',
            },
            {
                'title': 'life',
                'query': '/tag,wb-life',
            },
        ],
    },
    {
        'title': 'personal-tech',
        'children': [
            {
                'title': 'tech-your-life',
                'query': '/site,/technology/consumer-tech/tech-your-life',
            },
            {
                'title': 'tech-work',
                'query': '/site,/technology/consumer-tech/tech-work',
            },
            {
                'title': 'data-privacy',
                'query': '/site,/technology/consumer-tech/data-privacy',
            },
            {
                'title': 'internet-access',
                'query': '/site,/technology/consumer-tech/internet-access',
            },
            {
                'title': 'whats-new',
                'query': '/site,/technology/consumer-tech/whats-new',
            },
            {
                'title': 'ethical-issues',
                'query': '/site,/technology/consumer-tech/ethical-issues',
            },
        ],
    },
    {
        'title': 'world',
        'children': [
            {
                'title': 'africa',
                'query': '/site,/world/africa',
            },
            {
                'title': 'europe',
                'query': '/site,/world/europe',
            },
            {
                'title': 'americas',
                'query': '/site,/world/americas',
            },
            {
                'title': 'asia-pacific',
                'query': '/site,/world/asia-pacific',
            },
            {
                'title': 'middle-east',
                'query': '/site,/world/middle-east',
            },
        ],
    },
    {
        'title': 'usa',  # 'local' at washington post
        'children': [
            {
                'title': 'dc',
                'query': '/local-states,/local/dc,/local/dc/dc-politics,DC',
            },
            {
                'title': 'maryland',
                'query': '/local-states,/local/maryland,/local/maryland/md-politics,MD',
            },
            {
                'title': 'virginia',
                'query': '/local-states,/local/virginia,/local/virginia/vapolitics,VA',
            },
            {
                'title': 'public-safety',
                'query': '/site-articles-only,/local/public-safety',
            },
            {
                'title': 'education',
                'query': '/site,/local/education',
            },
            {
                'title': 'obituaries',
                'query': '/obits-stream',
            },
            {
                'title': 'traffic-commuting',
                'query': '/site,/local/traffic-commuting',
            },
        ],
    },
    {
        'title': 'sports',
        'children': [
            {
                'title': 'nfl',
                'query': '/site,/sports/nfl',
            },
            {
                'title': 'mlb',
                'query': '/site,/sports/mlb',
            },
            {
                'title': 'nba',
                'query': '/site,/sports/nba',
            },
            {
                'title': 'wnba',
                'query': '/two-sites,/sports/mystics,/sports/wnba',
            },
            {
                'title': 'nhl',
                'query': '/site-with-wires,/sports/nhl',
            },
            {
                'title': 'boxing-mma',
                'query': '/site-with-wires,/sports/boxing-mma',
            },
            {
                'title': 'colleges',
                'query': '/site,/sports/colleges',
            },
            {
                'title': 'golf',
                'query': '/site-with-wires,/sports/golf',
            },
            {
                'title': 'highschools',
                'query': '/site,/sports/highschools',
            },
            {
                'title': 'olympics',
                'query': '/site,/sports/olympics',
            },
            {
                'title': 'soccer',
                'query': '/site,/sports/soccer',
            },
            {
                'title': 'golf',
                'query': '/site-with-wires,/sports/tennis',
            },
        ],
    },
    {
        'title': 'abortion',
        'children': None,
        'query': '/tt-or-two-or-utility-tag-with-transparency-labels,77206,77450,abortion,News,Analysis,Perspective,Advice,$8,$9/',
    },
    {
        'title': 'entertainment',
        'children': [
            {
                'title': 'art',
                'query': '/site,/entertainment/museums',
            },
            {
                'title': 'movies',
                'query': '/site,/entertainment/movies',
            },
            {
                'title': 'music',
                'query': '/arts-music-feed/',
            },
            {
                'title': 'tv',
                'query': '/site,/entertainment/tv',
            },
            {
                'title': 'theater',
                'query': '/site,/entertainment/theater-dance',
            },
            {
                'title': 'video-games',
                'query': '/two-sites,/entertainment/video-games,/sports/launcher',
            },
            {
                'title': 'comics',
                'query': '/site,/entertainment/comics',
            },
        ],
    },
    {
        'title': 'business',
        'children': [
            {
                'title': 'cryptocurrency',
                'query': '/site,/business/cryptocurrency',
            },
            {
                'title': 'on-small-business',
                'query': '/site-with-wires,/business/on-small-business',
            },
            {
                'title': 'technology',
                'query': '/site-articles-only,/technology',
            },
        ],
    },
    {
        'title': 'economic-policy',
        'children': None,
        'query': '/site,/us-policy/economic-policy',
    },
    {
        'title': 'economy',
        'children': None,
        'query': '/site,/business/economy',
    },
    {
        'title': 'energy',
        'children': None,
        'query': '/site,/business/energy',
    },
    {
        'title': 'health-care',
        'children': None,
        'query': '/business-health-care/',
    },
    {
        'title': 'personal-finance',
        'children': None,
        'query': '/personal-finance/',
    },
    {
        'title': 'food',
        'children': [
            {
                'title': 'how-to',
                'query': '/site-and-tag,/lifestyle/food/voraciously,how-to',
            },
            {
                'title': 'news',
                'query': '/site-and-tag,/lifestyle/food/voraciously,trending',
            },
        ],
    },
    {
        'title': 'gender-identity',
        'children': [
            {
                'title': 'comics',
                'query': '/tag,GenderIdentity-Comics',
            },
            {
                'title': 'voices',
                'query': '/tag,GenderIdentity-Voices',
            },
            {
                'title': 'workday',
                'query': '/tag,GenderIdentity-Workday',
            },
            {
                'title': 'more-stories',
                'query': '/tag,genderidentity',
            },
        ],
    },
    {
        'title': 'health',
        'children': [
            {
                'title': 'medical-mysteries',
                'query': '/author,sandra-g-boodman',
            },
        ],
    },
    {
        'title': 'history',
        'children': None,
        'query': '/site,/history'
    },
    {
        'title': 'made-by-history',
        'children': None,
        'query': '/site,/opinions/made-by-history'
    },
    {
        'title': 'lifestyle',
        'children': [
            {
                'title': 'home-garden',
                'query': '/site-and-discussions-not-future,/lifestyle/home-garden',
            },
            {
                'title': 'on-parenting',
                'query': '/site-and-discussions-not-future,/lifestyle/on-parenting',
            },
        ],
    },
    {
        'title': 'immigration',
        'children': None,
        'query': '/site,/immigration'
    },
    {
        'title': 'national',
        'children': [
            {
                'title': 'investigations',
                'query': '/site,/national/investigations',
            },
            {
                'title': 'morning-mix',
                'query': '/site,/national/morning-mix',
            },
        ],
    },
    {
        'title': 'military',
        'children': None,
        'query': '/site,/national-security/military'
    },
    {
        'title': 'justice',
        'children': None,
        'query': '/site,/national-security/justice'
    },
    {
        'title': 'religion',
        'children': None,
        'query': '/site,/religion'
    },
    {
        'title': 'science',
        'children': None,
        'query': '/site,/science'
    },
    {
        'title': 'space',
        'children': None,
        'query': '/site,/technology/space'
    },
    {
        'title': 'animals',
        'children': None,
        'query': '/site,/science/animals'
    },
    {
        'title': 'transportation',
        'children': None,
        'query': '/two-sites,/local/traffic-commuting,/transportation'
    },
    {
        'title': 'travel',
        'children': [
            {
                'title': 'news',
                'query': '/primary-site,/travel',
            },
            {
                'title': 'tips',
                'query': '/site,/travel/tips',
            },
        ],
    },
    {
        'title': 'weather',
        'children': [
            {
                'title': 'extreme-weather',
                'query': '/site,/climate-environment/extreme-weather',
            },
            {
                'title': 'hurricanes-tropical-storms',
                'query': '/tt-or-story-tag-with-excluded-site,77663,hurricanes,/sports/',
            },
        ],
    },
]
