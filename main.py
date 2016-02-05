import os
import jinja2
import webapp2

lesson_notes = """
    <section class="section">
      <h2 class="subheading">The Internet</h2>
        <p class="text">The internet is a network of computers communicating
         with each other through the use of HTTP requests. Client computers
         request <em>HTML</em> documents from web servers &lpar;any computer
         hosting a file can be a server though "servers" usually refer to
         dedicated platforms&rpar; through the internet. The server sends the
         HTML file to the client computer where a browser interprets and
         displays the file. </p>
        <p class="text">Most Alaskans know that the internet is not a series
         of tubes.</p>
    </section>
"""

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPage(Handler):
    def get(self):
#       output = lesson_notes
#       self.write(output)
        self.render("lesson_notes.html")

app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
