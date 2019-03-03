from bottle import get, post, request, route, static_file, run, error

@error(404)
def error404(error):
    return 'Bobby is good at Riven'

@route('/')
def server():
    return static_file("page.html", root = "")

#@post('/join')
#def users():
#body for usernames
#   return user #and add it the game

#@post('/leave')
#def rageQuit():
#looks for usuer then removes it
#   return removed

#get

run(host = '0.0.0.0', port = 8080, debug = True)
