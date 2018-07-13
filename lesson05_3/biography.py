import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response('200 OK', headers)
    path = environ['PATH_INFO']
    if path == '/biography':
        page = '''<!DOCTYPE html>
            <HTML>
            <head><title>Biography</title></head><body>
            <h1>Hi, I'm Nathan</h1>
            <h2>My life</h2>
            
