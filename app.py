from flask import Flask, render_template, redirect
import os, pypandoc, random


app = Flask(__name__)

global inverted
global navbar

inverted = False
def update_navbar():
    return [str(file)[:-3] for file in os.listdir("resources")]

@app.route("/")
def index():
    return render_template("index.min.html", navbar=update_navbar(), colors=inverted)

@app.route("/<chapter>")
def give_me(chapter):
    try:
        file_to_compile = "resources/"+chapter+".md"
        this = pypandoc.convert_file(file_to_compile, 
        to='html5', 
        format='md', 
        extra_args=['--standalone', '--mathjax'])
    except :
        return render_template('error.min.html',  navbar=update_navbar(), colors=inverted)
    return render_template("chapters.min.html", navbar=update_navbar(), chapter=this, colors=inverted)

@app.route("/_invert")
def invert_colors():
    global inverted
    inverted ^= 1
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
        return render_template('error.min.html', navbar=update_navbar(), colors=inverted)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
