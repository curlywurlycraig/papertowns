import requests
from secrets import GOOGLE_API_KEY
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize

TEXT_SEARCH_URL = u'https://maps.googleapis.com/maps/api/place/textsearch/json?key=' + GOOGLE_API_KEY

# returns a pair: lat and long
def get_longitude_and_latitude(place_name):
    request_url = TEXT_SEARCH_URL + u'&query={}'.format(place_name)
    response = requests.get(request_url).json()

    result = response['results'][0]['geometry']['location']
    print "Lat and long: {}".format(result)
    return tuple(result.values())

def place_name_from_reddit_title(title):
    tagged_tree = ne_chunk(pos_tag(word_tokenize(title)))

    # duck typing - if the node has a _label attribute then it must be
    # a real node (and not just a tuple). In this case, ensure that its label is GPE
    # (a place) and return the place string
    for node in tagged_tree:
        if hasattr(node, '_label') and node._label == 'GPE':
            # return the first place name found
            return node[0][0]

    return None

def lat_long_from_reddit_title(title):
    # determine the place name from the title

    print u"Title: {}".format(title)
    place_name = place_name_from_reddit_title(title)
    print u"Found place name: {}\nfrom title {}".format(place_name, title)

    # return the lat and long as returned from gmaps api
    if place_name is None:
        return None

    return get_longitude_and_latitude(place_name)

