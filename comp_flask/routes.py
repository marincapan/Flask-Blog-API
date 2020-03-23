from . import comp_app
from flask import request
from flask import render_template

posts = {
    1: {
        'title': "#SUMMERTIME!",
        'author': "PitajaMan",
        'date': '26.07.2019.',
        'body': "Vrijeme je za ljetne praznike, ekipa uživajte..."
    },
    2: {
        'title': "COMP kreće u AKCIJU!",
        'author': "PitajaMan",
        'date': '10.10.2019.',
        'body': "Počela je nova akademska godina, a time smo osigurali i... "
    },
    3: {
        'title': "Linux InstallFest 2019!",
        'author': "PitajaMan",
        'date': '12.11.2019.',
        'body': "Održali smo još jedan uspješan Installfest..."
    }
}


@comp_app.route('/index')
def index():
    title = "Naslovnica"
    return render_template("index.html",
                           title=title
                           )


@comp_app.route('/blogs', methods=['GET'])
def get_blogs():
    title = "Svi blogovi"
    return render_template("news.html",
                           title=title,
                           blogs=posts
                           )


@comp_app.route('/blogs/<blog_id>', methods=['POST'])
def show_blog(blog_id):
    post = posts[int(blog_id)]
    title = "Jedan blog"
    return render_template("news_post.html",
                           title=title,
                           blog=post
                           )


