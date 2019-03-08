from bottle import get, post, request, route, static_file, run, error, response


@route('/')
def server():
    return static_file("page.html", root="")


@route('/image')
def image():
    return static_file("ChronoTrigger.jpg", root="")


@route("/cookie")
def cookie():
    return static_file("cookie.js", root="")


@post('/addName')
def addnewUser():
    return static_file("username.js", root="")


@get('/getNameList')
def allNameinList():
    return static_file("username.js", root="")


@error(404)
def error404(error):
    return "That's it, time to switch major!"


run(host="localhost", port=8080, debug=True)
