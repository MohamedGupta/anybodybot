import oauth2, json


def oauth_req(url, key, secret, http_method='GET', post_body='', http_headers=None):
    consumer_key = ""
    consumer_secret = ""

    consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)

    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

def oauth_post(url, key, secret, http_method='POST', post_body='', http_headers=None):
    consumer_key = ""
    consumer_secret = ""

    consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)

    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


req = oauth_req('https://api.twitter.com/1.1/followers/ids.json',
                '', '')

id_dict = json.loads(req)
for id in id_dict['ids']:
    req2 = oauth_post('https://api.twitter.com/1.1/blocks/create.json?id={0}'.format(id),
                '', '')
