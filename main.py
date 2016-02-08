import os
import jinja2
import webapp2

"""
Sets up the Jinja2 environment by specifying the location of the HTML
templates and telling it to load them.
"""
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
    """Uses webapp2's request handler method to serve webpages."""

    def write(self, *args, **kwargs):
        # Actually creates the webpage
        self.response.write(*args, **kwargs)

    def render_str(self, template, **params):
        # Retrieves the template from template_dir
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        # Combines the above functions to create a webpage using the template
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    def get(self):
        self.render("main_page.html")


class WebBasics(Handler):
    def get(self):
        self.render("web_basics.html")


class HTMLNotes(Handler):
    def get(self):
        self.render("html_notes.html")

class CSSNotes(Handler):
    def get(self):
        self.render("css_notes.html")

class TipsAndTricks(Handler):
    def get(self):
        self.render("tips_and_tricks.html")

class PythonNotes(Handler):
    def get(self):
        self.render("python_notes.html")

app = webapp2.WSGIApplication([("/", MainPage),
                               ("/web_basics", WebBasics),
                               ("/html_notes", HTMLNotes),
                               ("/css_notes", CSSNotes),
                               ("/tips_and_tricks", TipsAndTricks),
                               ("/python_notes", PythonNotes),
                               ], debug=True)
