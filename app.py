from flask import Flask, render_template
import os, pypandoc, random


app = Flask(__name__)

navbar = []
for file in os.listdir("resources"):
    navbar.append(str(file)[:-3])


@app.route("/")
def index():
    return render_template("index.html", navbar=navbar)


@app.route("/<chapter>")
def give_me(chapter):
    file_to_compile = "resources/"+chapter+".md"
    this = pypandoc.convert_file(file_to_compile, 'html')

    return render_template("chapters.html", navbar=navbar, chapter=this)




if __name__ == '__main__':
    app.run(host="0.0.0.0")
