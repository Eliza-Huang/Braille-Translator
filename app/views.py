# views.py
# controlls the htiml pages and file uploading

import os, sys
from flask import request, redirect, url_for, send_from_directory, render_template

from app import app
from .models import splitImage

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'JPG', 'jpeg', 'gif'])

word = "hi"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename, file=sys.stderr)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filePath)
            global word
            word = splitImage(filePath)
            print(word, file=sys.stderr)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template("index.html")

@app.route('/<filename>')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/static/uploads/' + filename
    print(os.path.isfile(filename), file=sys.stderr)
    print(word, file=sys.stderr)
    return render_template('about.html', filename=filename, word=word)

@app.route('/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
