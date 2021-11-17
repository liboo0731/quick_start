
import web

web.config.debug = False
urls = (
    '/', 'Index',
    '/add', 'Add'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout', globals={})


class WebDB:
    def __init__(self):
        self.db = web.db.database(dbn='sqlite', db='hello.db')


class Index(WebDB):
    def GET(self):
        todos = self.db.select('todos')
        data = [dict(x) for x in todos]
        return render.index(data)


class Add(WebDB):
    def POST(self):
        i = web.input()
        print(i)
        n = self.db.insert('todos', name=i.name, title=i.title, num=i.num)
        raise web.seeother('/')


if __name__ == "__main__":
    app.run()
