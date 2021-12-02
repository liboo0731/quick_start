
import json

from utils.bottle import Bottle
from utils.bottle import response
from utils.bottle import view

from app01 import CONST_APP
from utils.bottle_rest import bottle_rest
from utils.model import DBTools

app = Bottle()


@app.error(404)
@app.error(405)
@app.error(500)
def err500(error):
    return json.dumps({'code': response.status_code, 'data': []})


@app.get(CONST_APP.SUB_URL)
@app.post(CONST_APP.SUB_URL)
@app.get(f'{CONST_APP.SUB_URL}/<id:int>')
@app.post(f'{CONST_APP.SUB_URL}/<id:int>')
@app.delete(f'{CONST_APP.SUB_URL}/<id:int>')
def app_rest(id=None):
    data = bottle_rest(CONST_APP.DATABASE, CONST_APP.TABLE_NAME_APP01, 'id', id)
    return data


@app.get('/form')
@view('form.tpl')
def app_form():
    db = DBTools(CONST_APP.DATABASE)
    table_headers = db.get_table_header(CONST_APP.TABLE_NAME_APP01)
    return {
        'data': {
            'table_headers': table_headers,
            'action_url': f'/{CONST_APP.PREFIX_APP01}{CONST_APP.SUB_URL}'
        }
    }
