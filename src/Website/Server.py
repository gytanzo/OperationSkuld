from bottle import get, post, request, route, static_file, run, error


@route('/')
def server():
    return static_file("page.html", root = "")

@post('/join')
def addusers():
    new_user = request.forms.get(input)
    return username

#@post('/leave')
#def rageQuit():
#looks for usuer then removes it
#   return removed

#get

#@error(404)
#def error404(error):
    return "I like women with BIG personalities."


run(host = '0.0.0.0', port = 8080, debug = True)
