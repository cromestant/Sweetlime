import sublime
import sublime_plugin
import json

class CheckServerCommand(sublime_plugin.WindowCommand):
    data ={"org": False, "username":False}
    def run(self):
        print("run")
        self.getOrg()
    def getOrg(self):
    	print('in org')
    	if self.data['org']:
    		print("got org")
    		self.org = self.data['org']
    	else:
    		self.window.show_input_panel("Org name:","",self.done_org,None,self.cancel)
    def getUser(self):
    	print("in get user")
    	if self.data['username']:
    		print("got user")
    		self.username = self.data['username']
    	else:
    		self.window.show_input_panel("Username:","",self.done_user,None,self.cancel)
    def done_org(self,data):
    	print("in done Org")
    	self.org= data
    	self.getUser();
    def done_user(self,data):
    	print('in done user')
    	self.username= data
    def cancel(self):
    	print("user cancelled")