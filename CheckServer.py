import sublime
import sublime_plugin
import json,base64
import urllib.request, urllib.parse

class CheckServerCommand(sublime_plugin.WindowCommand):
      #data ={"org": False, "username":False}
    def run(self):
        json_data=open(self.window.folders()[0]+'/deploy_vars.json')
        self.data = json.load(json_data)
        json_data.close()
        print(self.data)
        self.getOrg()
    def getOrg(self):
        if self.data['org']:
            self.org = self.data['org']
            self.getEnv()
        else:
            self.window.show_input_panel("Org name:","",self.done_org,None,self.cancel)
    def getEnv(self):
        if self.data['env']:
            self.env = self.data['env']
            self.getUser()
        else:
            self.window.show_input_panel("Environment:","",self.done_env,None,self.cancel)
    def getUser(self):
        if self.data['username']:
            self.username = self.data['username']
            self.getPassword()
        else:
            self.window.show_input_panel("Username:","",self.done_user,None,self.cancel)
    def getPassword(self):
        if self.data['password']:
            self.password=self.data['password']
            self.fetch_data()
        else:
            self.window.show_input_panel("Password:","",self.done_password,None,self.cancel)
    def fetch_data(self):
        print(self.data)
        bs64 = base64.encodestring(('%s:%s' % (self.username,self.password)).encode('utf-8'))[:-1]
        url = self.data['uri'] or "https://api.enterprise.apigee.com"
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, url,self.username,self.password)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        opener.open("%s/v1/o/%s/environments/%s/targetservers" %(url,self.org,self.env))
        print(opener.read())



        #sublime.message_dialog("Message goes here.")

    def done_env(self,data):
        self.env =env
        self.getUser()
    def done_org(self,data):
        self.org= data
        self.getEnv()
    def done_user(self,data):
        self.username= data
        self.getPassword()
    def done_password(self,data):
        self.password= data
        self.fetch_data()
    def cancel(self):
        print("user cancelled")