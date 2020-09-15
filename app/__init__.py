import os

from flask import (Flask, render_template, request, redirect, send_file, url_for)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass   

    app.config["IMAGE_UPLOADS"] = os.path.join(os.path.abspath(os.path.dirname("")), 'static')

    # == routes ==
    @app.route('/', methods=['GET', 'POST'])
    def index():
        
        if request.method == 'POST':

            if request.files:
                options = request.form["options"]
                image = request.files["image"]
                path = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
                print(options)
                print(path)
                print(image)
                image.save(path)
                return redirect(url_for('index'))

        return render_template('/index.html')

    return app