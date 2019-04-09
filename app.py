from flask import Flask, render_template, redirect
import os, pypandoc, random


app = Flask(__name__)

def update_navbar():
    return sorted([str(file)[:-3] for file in os.listdir("resources")])

@app.route("/")
def index():
    return render_template("index.min.html", navbar=update_navbar())

@app.route("/<chapter>")
def give_me(chapter):
    try:
        file_to_compile = "resources/"+chapter+".md"
        this = pypandoc.convert_file(file_to_compile, 
        to='html5', 
        format='md', 
        extra_args=['--standalone', '--mathjax'])
    except :
        return render_template('error.min.html',  navbar=update_navbar())
    return render_template("chapters.min.html", navbar=update_navbar(), chapter=this)


@app.errorhandler(404)
def page_not_found(e):
        return render_template('error.min.html', navbar=update_navbar())

if __name__ == '__main__':
    app.run(host="0.0.0.0")
