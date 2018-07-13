import wsgiref.simple_server
import random
import urllib.parse
from database import Simpledb

fortune = [
    'Be a generous friend and a fair enemy.',
    '傷心有多少 在乎就有多少',
    'A bargain is something you don\'t need at a price you can\'t resist.',
    'A single conversation with a wise man is better than ten years of study.',
    'All the water in the world can\'t sink a ship unless it gets inside.',
    'Ask a friend to join you on your next voyage.',
    'Back away from individuals who are impulsive.',
    'Bad luck and misfortune will follow you all your days.',
    'Be a good friend and a fair enemy.',
    'Bread today is better than cake tomorrow.',
    'Circumstance does not make the man; it reveals him to himself.',
    'Cookie says, "You crack me up."',
    'Do not be covered in sadness or be fooled in happiness;  they both must exist.',
    'Do not fear what you don\'t know.',
    'Do not follow where the path may lead. Go where there is no path...and leave a trail.'
]

def fortune_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    db = Simpledb('db.txt')

    if path == '/insert':
        db.insert(params['key'][0], params['value'][0])
        return ['inserted'.encode()]


    #return [random.choice(fortune).encode()]

httpd = wsgiref.simple_server.make_server('', 8000, fortune_app)
print("Serving on port 8000...") #This prints a line in your IDE to say your server is running correctly

httpd.serve_forever()
