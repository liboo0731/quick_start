from bottle import route
from bottle import view
from bottle import template
from bottle import request
from bottle import abort
from bottle import redirect
from bottle import static_file
from bottle import error
from bottle import get
from bottle import post
from bottle import Bottle
from bottle import run


@error(404)
def error404(error):
    return 'Nothing here, sorry'


@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")


@route('/wrong/url')
def wrong():
    redirect("/right/url")


@route('/hello1')
@route('/hello1/<name>')
def hello1(name='World'):
    return template('hello_template', name=name)


@route('/hello')
@route('/hello/<name>')
@view('hello_template')
def hello(name='World'):
    return dict(name=name)


@route('/login1')
def login1():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@route('/login1', method='POST')
def do_login1():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    pass


@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)


@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='/path/to/image/files', mimetype='image/png')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/path/to/static/files')


@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/path/to/static/files', download=filename)


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/path/to/your/static/files')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/path/to/your/static/files')


app = Bottle()


@app.route('/hello')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # run(app, host='localhost', port=8080)
    run(host='localhost', port=8080, debug=True)
