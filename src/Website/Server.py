from bottle import get, post, request, route, static_file, run, error


@route('/')
def server():
    return static_file("page.html", root="")

#@post('/join')
#def addUsers():
#    new_user = {"Username" : request.json.get('Username'), 'Status' : request.json.get('Status')}
#    User.append(new_user)
#    return {"User"" : User}
#textfile name will be Users
#user name will be the key and name will be the value
#Username : namess and Status  for json string ingame, quit


#@get('/all')
#def allUsers():
#    all_user =
 #   return {"Username" : Username, "Stats", Status}

@error(404)
def error404(error):
    return "You should watch A Place Further Than The Universe."


run(host='0.0.0.0', port=8080, debug=True)
