from bottle import get, post, request, route, static_file, run, error


@route('/')
def server():
    return static_file("page.html", root = "/FrontEnd")

#@post('/join')
#def users():
#body for usernames
#ex:def do_login():
    #username = request.forms.get('username')
    #password = request.forms.get('password')
    #if check_login(username, password):
     #else:
        #return "<p>Login failed.</p>"
#   return user #and add it the game

#@post('/leave')
#def rageQuit():
#looks for usuer then removes it
#   return removed

#get

@error(404)
def error404(error):
    return "I like women with BIG personalities."


run(host = '0.0.0.0', port = 8080, debug = True)
