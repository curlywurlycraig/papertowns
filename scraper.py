import praw
from datastorage import Town
from datastorage import session
from place_search import lat_long_from_reddit_title

praw_client = praw.Reddit(user_agent='papertowns scraper')

# how many hot submissions should we grab?
SCRAPER_LIMIT = 10

# pull in top papertowns posts
def scrape_top_papertowns_posts():
    submissions = praw_client.get_subreddit('papertowns').get_hot(limit=SCRAPER_LIMIT)

    for submission in submissions:
        encoded_title = submission.title.encode('utf-8')

        lat_and_long = lat_long_from_reddit_title(encoded_title)
        if lat_and_long is None:
            continue
        else:
            latitude, longitude = lat_and_long

        # check to see if a post already exists with this submission url
        existing = session.query(Town).filter(Town.submission_url==submission.permalink).count()
        if existing > 0:
            continue

        # create the new entry
        town = Town(title = encoded_title,
                    image_url = submission.url,
                    submission_url = submission.permalink,
                    longitude = longitude,
                    latitude = latitude)
        session.add(town)

    session.commit()

scrape_top_papertowns_posts()
