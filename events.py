import urllib2, os, json
from pprint import pprint
key = os.environ['MEETUP_API_KEY']
for i in range(1, 1001):
    member_id = str(i)
    url = 'https://api.meetup.com/2/events?key={0}&sign=true&photo-host=public&member_id={1}&limited_events=true&page=20'
    url = url.format(key, member_id)
    pprint(url)
    out = json.loads(urllib2.urlopen(url).read())
    signed_url = out['meta']['signed_url']
    pprint(signed_url)
    signed_out = json.loads(urllib2.urlopen(signed_url).read())
    pprint(signed_out['results'])
