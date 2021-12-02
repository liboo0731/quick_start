
from utils.bottle import Bottle
from utils.bottle import view
from utils.bottle import static_file

from app01 import app01, CONST_APP


root = Bottle()
root.mount(CONST_APP.PREFIX_APP01, app01.app)


@root.get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='views/static/')


@root.get('/')
@view('index.tpl')
def index():
    return


if __name__ == '__main__':
    from gevent import monkey

    monkey.patch_all()

    from gevent.pool import Pool
    from gevent.pywsgi import WSGIServer
    from utils.bottle import Bottle

    pool = Pool(256)
    server = WSGIServer(('0.0.0.0', 8080), root, spawn=pool)
    server.backlog = 256
    server.max_accept = 30000
    server.serve_forever()
