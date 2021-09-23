#!/usr/bin/env python3
import cgi
import cgitb, os
import secret 
from templates import _wrapper, login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie

cgitb.enable()

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

cookie = SimpleCookie(os.environ['HTTP_COOKIE'])

cookie_username = None
cookie_password = None

if (cookie_username == cookie.get("username")):
    username = cookie_username

if (cookie_password == cookie.get("password")):
    password = cookie_password

print("Content-Type: text/html")

if ((username == secret.username) and (password == secret.password)):
    print (f'Set-Cookie: username=sudo')
    print (f'Set-Cookie: password=123')

if not username and not password:
    print (login_page())
elif (username == secret.username and password == secret.password):
    print (secret_page(username, password))
else:
    print (after_login_incorrect())



print (os.environ.keys())



