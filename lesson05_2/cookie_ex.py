import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Set-Cookie', 'name=Jason'),
               ('Set-Cookie', 'favoriteNumber=4'),
               ('Set-Cookie', 'favoriteColor=red')]

    if 'HTTP_COOKIE' in environ:
        print("Environ"+str(environ["HTTP_COOKIE"]))
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        res = ""
        for key in cookies:
            print(str(cookies))
            print ("Cookie key name="+str(cookies["name"].value))
            if cookies["name"]=="Jason":
                cookies["name"]="Nathan"
            res += (key + ": " + cookies[key].value + "\n")
        start_response('200 OK', headers)
        return[res.encode()]
    else:
        start_response('404 Not Found' , headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()