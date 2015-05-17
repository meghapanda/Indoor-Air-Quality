import web
import requests

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        a=requests.get('https://api.thingspeak.com/channels/31959/feeds.json')

	Apdjfkfh
	a.json()
	return 
	

if __name__ == "__main__":
    app.run()
