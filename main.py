from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import util
from google.appengine.api import mail
 
class BugData(db.Model):
    app_name = db.StringProperty()#application name
    device = db.StringProperty()#device name
    model = db.StringProperty()#model name
    sdk = db.StringProperty()#sdk name
    version = db.StringProperty()#version number
    bug = db.TextProperty()#stacktrace
    create = db.DateTimeProperty(auto_now_add=True)
 
class BugReportHandler(webapp.RequestHandler):
 
    def get(self):
        self.get_or_post()
 
    def post(self):
        self.get_or_post()
 
    def get_or_post(self):
        app_name = self.request.get("app")
        dev = self.request.get("dev")
        mod = self.request.get("mod")
        sdk = self.request.get("sdk")
        ver = self.request.get("ver")
        bug  = self.request.get("bug")

        if app_name == None:
            app_name = "Unknown App"

        #insert new element
        db = BugData(app_name=app_name, device=dev, model=mod, sdk=sdk, version=ver, bug=bug)
        db.put()
 
        #report with email
        #mail.send_mail(sender="developer@gmail.com", to="developer@gmail.com", subject="Bug Report", body=bug)
 
        self.response.out.write('Success!')
 
def main():
  application = webapp.WSGIApplication([('/bug', BugReportHandler)],
                                       debug=False)
  util.run_wsgi_app(application)
 
 
if __name__ == '__main__':
  main()

