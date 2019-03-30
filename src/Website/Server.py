from bottle import get, post, request, route, static_file, run, error, response
import json
import Website.BackEnd_key
import  Website.user
@route('/')
def server():
    return static_file("page.html", root="")


@route('/image')
def image():
    return static_file("ChronoTrigger.jpg", root="")


@route('/backEndkey')
def backend_key():
    return Website.BackEnd_key.send_key("")


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
    return "Holy fucking shit. I want to bang Zero Two so goddamn bad. I can't stand it anymore. Any time there’s a scene with Zero Two, I get a massive erection. I've seen literally every rule 34 post there is of her online. My dreams are nothing but constant fucking sex with Zero Two. I'm sick of waking up every morning with six nuts in my boxers and knowing that those are nuts that should've been busted inside of Zero Two’s tight dino pussy. God I wish I was Hiro because I fucking know for a fact that Zero Two drains his balls daily. I want her to suck all of my humanity out and ride me to death. Anyways, do you guys relate to this?"


run(host="localhost", port=8080, debug=True)
