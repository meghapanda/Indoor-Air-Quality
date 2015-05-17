import web

urls = (
  '/', 'hello',
  '/bye/', 'bye')

app = web.application(urls, globals(), True)

render = web.template.render('templates/')

class hello:
    def GET(self):
        return render.hello("Templates demo", "Hello", "A long time ago...")


if __name__ == "__main__":
    app.run()
