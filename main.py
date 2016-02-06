import os
import jinja2
import webapp2

"""
"""
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    """Uses webapp2's request handler method to serve webpages."""
    def write(self, *args, **kwargs):
        """Actually creates the webpage"""
        self.response.write(*args, **kwargs)

    def render_str(self, template, **params):
        """Retrieves the template from template_dir"""
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        """Combines the above functions to create a webpage using the template"""
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    def get(self):
        self.render("main_page.html")

app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
