#The orginal basis of this code was from https://learnpythonthehardway.org/book/ex52.html
import web
import os
import sys

#from gothonweb import map

urls = ('/(.*)/'   , 'redirect'   #redirect without trailing /
       ,'/'        , 'Index'
       ,'/repolist', 'RepoList'
)

app = web.application(urls, globals())

#Start from app.py (python script and go up 2 dirs)
#web_root = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
#web.debug(web_root)
#Then go down 3 dirs - this is the new root that web addresses will be related to.
#Eg release/share/git-webui/webui/ (css|img|js)
#web_root = os.path.join(web_root, "share", "git-webui", "webui")

# little hack so that debug mode works with sessions
#if web.config.get('_session') is None:
#    store = web.session.DiskStore('sessions')
#    session = web.session.Session(app, store,
#                                  initializer={'SQLsession': None})
#    web.config._session = session
#else:
#    session = web.config._session

#render = web.template.render('templates/', base="layout")

#Find the root of the app
app_root = os.path.dirname(os.path.dirname(__file__))  #Start from app.py (python script and go up 2 dirs)
web.debug(app_root)
tempates_dir = os.path.join(app_root,'templates/')
web.debug(tempates_dir)
render = web.template.render(tempates_dir, globals=globals(), base="layout")

#workaround for missing host details
def full_url(path):
    return 'https://'+web.ctx.host+'/'+path
    
def seeother(path):
    raise web.seeother(full_url(path))  
    
    
class redirect:
    def GET(self, path):
        #This effectively removes the trailing / and retries it.
        #raise web.seeother('https://'+web.ctx.host+'/' + path)
        seeother(path)

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        #session.SQLsession = None
        seeother('repolist')
        #raise web.seeother(full_url('repolist'))  


class RepoList(object):

    def GET(self):
        return render.repo_list()  
        #if session.room:
        #    return render.repo_list()
        #else:
            # why is there here? do you need it?
        #    return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        #if session.room and form.action:
        #    session.room = session.room.go(form.action)
  
        seeother('repolist')
        #raise web.seeother(full_url('repolist'))  

if __name__ == "__main__":
    app.run()