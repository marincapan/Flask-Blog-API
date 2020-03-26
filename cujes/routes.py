from cujes import cujes_app as app
from flask import render_template
from .models import Season, Artist, Post, Application


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
        'author': "LVH-27",
        'date': '12.11.2019.',
        'body': "Održali smo još jedan uspješan Installfest..."
    }
}


bands = {
    1: {
        'name': "K3P",
        'town': "Zagreb",
        'genre': "ska punk1",
        'bio': "k3p bio"
    },
    2: {
        'name': "K4P",
        'town': "Zagreb2",
        'genre': "punk ska2",
        'bio': "k3p bio2"
    },
    3: {
        'name': "K5P",
        'town': "Zagreb3",
        'genre': "ska-punk3",
        'bio': "k3p bio3"
    }
}


@app.route('/')
@app.route('/index')
def index():
    title = "Flask-Blog"
    return render_template("index.html",
                           title=title,
                           bands=bands
                           )


@app.route('/blogs')
def news():
    title = "Blogs"
    return render_template("news.html",
                           title=title,
                           bands=bands,
                           posts=posts,
                           )


@app.route('/blogs/id/<post_id>')
def news_post(post_id):
    title = "Blog"
    if int(post_id) in posts:
        post = posts[int(post_id)]
        return render_template("news_post.html", bands=bands, post=post, title=title)
    else:
        return render_template("404.html")
        
@app.route('/blogs/author/<post_author>')
def news_post_author(post_author):
    title = "Blogovi Autora"
    new_posts={}
    for k,v in posts.items():
        if v['author']==post_author:
            new_posts[k]=posts[k]
    return render_template("news.html",
                           title=title,
                           bands=bands,
                           posts=new_posts,
                           )

@app.route('/blogs/search/<post_string>')
def news_post_search(post_string):
    title = "Rezultati traženja"
    new_posts={}
    for k,v in posts.items():
        if post_string in v['body']:
            new_posts[k]=posts[k]
    return render_template("news.html",
                           title=title,
                           bands=bands,
                           posts=new_posts,
                           )                
    

@app.route('/izvodaci/<band_id>')
def band_post(band_id):
    band = bands[int(band_id)]
    return render_template("band_page.html",
                           bands=bands,
                           band=band)


@app.route('/info')
def info():
    title = "Informacije"
    info = """Zmija organizira
sezone bendovi
tjedno jedan koncert za tri benda
finale u petom mjesecu
Prijave do x.y.2020."""
    contact = {"email": "cujes@kset.org",
               "facebook": "https://www.facebook.com/cujesKSET/"}

    return render_template("info.html",
                           title=title,
                           info=info,
                           contact=contact)


@app.route('/prijavi_se')
def apply():
    return "Prijava TODO NAKON BAZE"
