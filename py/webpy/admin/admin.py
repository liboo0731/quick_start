
import web

urls = (
    '/admin', 'Admin',
    '/admin/add', 'Add'
)
app_admin = web.application(urls, globals())
render = web.template.render('templates/', base='layout', globals={})


class WebDB:
    def __init__(self):
        self.db = web.db.database(dbn='sqlite', db='hello.db')


class Admin(WebDB):
    def GET(self):
        todos = self.db.select('todos')
        data = [dict(x) for x in todos]
        return render.admin(data)


class Add(WebDB):
    def POST(self):
        i = web.input()
        print(i)
        try:
            self.db.insert('todos', name=i.name, title=i.title, num=i.num)
        except Exception as e:
            print(e)
        raise web.seeother('/admin')
