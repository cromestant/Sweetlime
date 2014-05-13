import sublime
import sublime_plugin
import json

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
            self.getUser()
        else:
            self.window.show_input_panel("Org name:","",self.done_org,None,self.cancel)
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
    def done_org(self,data):
        self.org= data
        self.getUser();
    def done_user(self,data):
        self.username= data
        self.getPassword()
    def done_password(self,data):
        self.password= data
        self.fetch_data()
    def cancel(self):
        print("user cancelled")