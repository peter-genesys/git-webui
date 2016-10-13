
import web #The genesis of the use of web.py was from https://learnpythonthehardway.org/book/ex52.html
import os
#import sys
import json
from git import Repo
join = os.path.join

#from gothonweb import map

urls = ('/(.*)/'   , 'redirect'   #redirect without trailing /
       ,'/'        , 'Index'
       ,'/repolist', 'RepoList'
       ,'/repoconfig', 'RepoConfig'
       ,'/test'    , 'TestJquery'
)

app = web.application(urls, globals())
 
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
render = web.template.render(tempates_dir, globals=globals(), base="layout1")

#GLOBAL FUNCTIONS
#workaround for missing host details
def full_url(path):
    return 'https://'+web.ctx.host+'/'+path
    
def seeother(path):
    raise web.seeother(full_url(path))  
  
    
#CLASSES    
class redirect:
    def GET(self, path):
        seeother(path)

class Index(object):
    def GET(self):
        return render.index()  
        # this is used to "setup" the session with starting values
        #session.SQLsession = None
        #seeother('repolist')

class RepoList(object):

    def GET(self):
        return render.repo_list()  
        #if session.room:
        #    return render.repo_list()
        #else:
            # why is there here? do you need it?
        #    return render.you_died()

    def POST(self):
 
        print "POST"
        
        print web.data()
 
        json_data = json.loads(web.data())
 
        print json.dumps(json_data)
        
        print os.listdir(json_data["path"])
        
        path = json_data["path"]
        dirs = os.listdir(path)
        repos = []
        for folder in dirs:
            folder_path = path+'/'+folder
            if '.git' in os.listdir(folder_path):
                repo = Repo(folder_path)
                assert not repo.bare
                current_branch = repo.active_branch
                print current_branch.name
                repo = {'name':folder, 'path':folder_path,'branch':current_branch.name}
                repos.append(repo.copy())
        
        web.header('Content-Type', 'application/json')
        
        print json.dumps(repos)
        
        return json.dumps(repos)
      
        
'''    
        return json.dumps( [{
                'name': "Repo5",
                'path': "/home/ubuntu/GitRepos/CrowdMortgageLive",
                'branch': "develop"
                }
                ,{
                'name': "Repo6",
                'path': "/home/ubuntu/GitRepos/CrowdMortgageLive",
                'branch': "master"
                }]) 
        
 
        #process post request
        if self.path == "/refreshRepoList": 
            print "/refreshRepoList"
   
            user_data = web.input()
            
            data = web.data() # you can get data use this method
            print data
            response = json.dumps({'name'  : 'R1'
                                  ,'path'  : 'P1'
                                  ,'branch': 'B1' 
                                  }) + '\n' #add linefeed to help separate from footers

            self.wfile.write(response)
            self.send_response(200)
            
        else: 
            print "else"
            
            seeother('repolist')
'''
class RepoConfig(object):

    def GET(self):
        return render.repo_config()  
     
    def POST(self):
 
        print "RepoConfig"
        
        print web.data()
 
        json_data = json.loads(web.data())
 
        print json.dumps(json_data)
 
        GitReposConfigRelPath = json_data["path"]
        
        GitReposConfigAbsPath = os.path.join(app_root,GitReposConfigRelPath)
        
        print GitReposConfigAbsPath
        
        repoConfig = open(GitReposConfigAbsPath, 'r').read()
        
        web.header('Content-Type', 'application/json')
        
        return repoConfig
 

class TestJquery(object):

    def GET(self):
        return render.test_jquery()  


if __name__ == "__main__":
    app.run()