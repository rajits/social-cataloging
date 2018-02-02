import requests
from django.conf import settings

KEY = settings.KEYS.get('LibraryThing', 'KEY')
SIZES = ('small', 'medium', 'large')

def get_cover(key, size, isbn):
    '''
    retrieves a cover image
    '''
    url = 'http://covers.librarything.com/devkey/%s/%s/isbn/%s'
    return url % (key, size, isbn)

def get_work(apikey):
    VERSION = '1.1'
    METHOD_NAME = 'librarything.ck.getwork'
    url = 'http://www.librarything.com/services/rest/%s/?method=%s&id=1060&apikey=%s' % (VERSION, METHOD_NAME, key)
    response = requests.get(url)
