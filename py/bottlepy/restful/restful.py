
import json

from bottle import Bottle
from bottle import request
from bottle import response
from bottle import error
from bottle import run

from model import AppDB

app = Bottle()


def error_msg(code):
    return json.dumps({'code': code, 'data': []})


@error(404)
def err404(error):
    return error_msg(response.status_code)


@error(405)
def err405(error):
    return error_msg(response.status_code)


@error(500)
def err500(error):
    return error_msg(response.status_code)


@app.get('/app/list')
@app.post('/app/list')
@app.get('/app/list/<id:int>')
@app.post('/app/list/<id:int>')
@app.delete('/app/list/<id:int>')
def app_restful(id=None):
    db = AppDB('app.db')
    if request.method == 'POST':
        if id:
            data = db.execute(f'update from app set {} where id=?', [id])
        else:
            data = db.execute('insert from app values (?,?,?)')
    elif request.method == 'DELETE':
        data = db.execute('delete from app where id=?', [id])
    else:
        if id:
            data = db.execute('select * from app where id=?', [id])
        else:
            data = db.execute('select * from app')

    return json.dumps({'code': response.status_code, 'data': data})


if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port='8080')
