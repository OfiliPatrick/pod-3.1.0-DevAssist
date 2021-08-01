from flask import Flask, render_template, redirect, url_for, send_from_directory, request
from imports.ErrAutoSearch import main_func
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('landingPage.html')


@app.route('/autoErrCheck')
def fileupload():
    return render_template('stackOverflow.html')

@app.route('/websiteBlocker')
def websiteBlocker():
    return render_template('websiteBlocker.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect('/dashboard')
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = main_func()
            print(result)
            return render_template('stackOverflow.html', result=result)
    return redirect('/autoErrCheck')

# all the routes go here


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
