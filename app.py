from flask import Flask
from flask import render_template, flash, request, redirect, url_for
import os
import bibtexparser

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


def read_data():
    inproceedings = []
    article = []
    for file in os.listdir(app.static_folder):
        if file.split('.')[-1] == "bib":
            with open(os.path.join(app.static_folder, file)) as bibtex_file:
                bibtex_str = bibtex_file.read()
            data = bibtexparser.loads(bibtex_str).entries
            if data is None:
                continue
            if data[0]['ID'] == "inproceedings":
                inproceedings.append(data[0])
                continue
            if data[0]['ID'] == "article":
                article.append(data[0])
                continue
    return inproceedings, article


@app.route('/', methods=["GET", "POST"])
def home():
    inproceedings, article = read_data()
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
            return redirect(request.url)
    return render_template('index.html', inproceedings=inproceedings, article=article)


if __name__ == '__main__':
    app.run(debug=True)
