import os
from palette import Palette
from flask import Flask, redirect, url_for, render_template, request, flash
from flask_bootstrap import Bootstrap4
# if it doesnt work: terminal --> pip3 install bootstrap-flask
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

# TODO: ADD MESSAGE WHEN EXTENSION NOT ALLOWED IN THE FORM


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.secret_key = "my app secret key"
Bootstrap4(app)


@app.route("/",  methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/palette", methods=['POST', 'GET'])
def show_palette():
    if request.method == 'POST':
        num_colors = int(request.form['num_colors'])
        file = request.files['img_file']
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            my_palette = Palette(f'static/uploads/{filename}', num_colors)
            colors = my_palette.pal_array()
        else:
            #flash('Allowed image types are -> png, jpg, jpeg')
            return redirect(url_for('home'))
    return render_template('result.html', img_file=filename, colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
