import wsgiref.simple_server
import urllib.parse
from database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    db = Simpledb('db.txt')

    if path == '/insert':
        start_response('200 OK', headers)
        db.insert(params['key'][0], params['value'][0])
        return ['Inserted'.encode()]

    elif path == '/select':
        s = db.select_one(params['key'][0])
        start_response('200 OK', headers)
        if s:
            return [s.encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/delete':
        start_response('200 OK', headers)
        d = db.delete(params['key'][0])
        if d:
            return ['Deleted'.encode()]
        else:
            return ['NULL'.encode()]

    elif path == '/update':
        start_response('200 OK', headers)
        u = db.update(params['key'][0], params['value'][0])
        if u:
            return ['Updated'.encode()]
        else:
            return ['NULL'.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
'''
u=  "http://localhost:8000/insert?key=arjana&value=(801)555-1234"

environ={"PATH_INFO":"/insert", "QUERY_STRING":"key=arjana&value=(801)555-1234"}

print(application(environ,start_response)
'''