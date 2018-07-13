import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies

connection = sqlite3.connect('users.db')
cursor = connection.cursor()


try:
    connection.execute('DROP TABLE employees')
except:
    pass


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE uid = ?', [un]).fetchall()

        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:
            connection.execute('INSERT INTO users (uid, pwd) VALUES (?, ?)', [un, pw])
            connection.commit()
            start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8'), ('Set-Cookie', 'session=un:pw')])
            return ['Username {} was successfully registered'.format(un).encode()]

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE uid = ? AND pwd = ?', [un, pw]).fetchall()
        if user:
            start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8'), ('Set-Cookie', 'session={}:{}'.format(un, pw))])
            return ['User {} successfully logged in'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8'), ('Set-Cookie', 'session={}:{}; expires=Sun, 25 Dec 2016 00:15:49 GMT'.format(un, pw))])
        return ['Logged Out'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)
        if 'HTTP_COOKIE' in environ:
            cookies = http.cookies.SimpleCookie()
            cookies.load(environ['HTTP_COOKIE'])
            if 'session' in cookies:
                return ['Currently logged in'.encode()]
            else:
                return ['Currently logged out'.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
