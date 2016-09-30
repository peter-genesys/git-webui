import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('/home/ubuntu/workspace/demo/templates/')

class index:
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()