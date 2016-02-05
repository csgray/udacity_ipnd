import os
import jinja2
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        os.path = os.path.join(os.path.dirname(__file__), 'lesson_notes.html')
        self.response.out.write()

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
