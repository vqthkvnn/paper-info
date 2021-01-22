from flask import Flask
from flask import render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/', methods=["GET", "POST"])
def home():
    data = {'article': [{'title': 'Tiêu đều số 1', 'author': 'Tác giả số 1', 'year': '2019'},
                        {'title': 'Tiêu đều số 1', 'author': 'Tác giả số 1', 'year': '2020'}]}
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
            return redirect(request.url)
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run()
