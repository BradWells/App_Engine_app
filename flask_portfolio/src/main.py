from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

personal_url = 'http://www.bradleymwells.com'
resume_rel_url = 'resume'

class linkObj:
    """A container for relative links and their paired names"""
    def __init__(self, link, name):
        self.url = link
        self.name = name

projList = [
    linkObj("#Senior-Design-Project", "Senior Design"),
    linkObj("#Munchkin-on-Android", "Android Munchkin"),
    linkObj("#Fluid-Invitation-Website", "Invitation Website"),
    linkObj("#Other-Projects", "Other Projects")
    ]

@app.route('/')
def home():
    """The homepage of my site, a welcoming landing"""
    return render_template(
        'home.html',
        personal_url = personal_url,
        home_url = url_for('home'),
        title = "Home",
        projects = projList,
        )

@app.route('/about')
def about():
    """A page about who I am"""
    return render_template(
        'about.html',
        personal_url = personal_url,
        home_url = url_for('home'),
        title = "About",
        projects = projList
        )

@app.route('/contact')
def contact():
    """A page with my contact information"""
    return render_template(
        'contact.html',
        personal_url = personal_url,
        home_url = url_for('home'),
        title = "Contact",
        projects = projList
        )

@app.route('/projects')
def projects():
    """A page of my projects"""
    return render_template(
        'projects.html',
        personal_url = personal_url,
        home_url = url_for('home'),
        title = "Projects",
        projects = projList,
        test = url_for('projects')
        )

@app.rout('/resume.pdf')
def resume():
    return

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
