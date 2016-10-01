#The orginal basis of this code was from https://learnpythonthehardway.org/book/ex52.html
import web
import os
import sys

#from gothonweb import map

urls = (
  '/'        , 'Index'
 ,'/repolist', 'RepoList'
)

app = web.application(urls, globals())

#Start from app.py (python script and go up 2 dirs)
web_root = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
web.debug(web_root)
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

app_root = os.path.dirname(os.path.dirname(__file__))
web.debug(app_root)
render = web.template.render(os.path.join(app_root,'templates/'), globals=globals(), base="layout")

#workaround for missing host details
def full_url(path):
    return 'https://'+web.ctx.host+'/'+path

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        #session.SQLsession = None
        raise web.seeother(full_url('repolist'))  


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

        raise web.seeother(full_url('repolist'))  

if __name__ == "__main__":
    app.run()