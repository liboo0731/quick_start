
import web

from admin import admin
from demo import demo

urls = (
    '/', 'Index',
    '/demo', demo.app_demo,
    '', admin.app_admin
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout', globals={})


class Index:
    def GET(self):
        return render.index()


if __name__ == "__main__":
    web.config.debug = False
    app.run()
