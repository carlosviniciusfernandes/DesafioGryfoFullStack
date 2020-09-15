import os

from flask import (Flask, render_template, request, redirect, send_file, url_for)

from . import imgProcessing as ip

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
                image.save(path)
                return redirect(url_for('download', img=image.filename, options=options))

        return render_template('/index.html')
    
    @app.route('/download/<img>/<options>', methods=['GET', 'POST'])
    def download(img, options):
        path = os.path.join(app.config["IMAGE_UPLOADS"], img)
        ip.processCheckedOptions(path, options)
        return render_template('/download.html', img=img)

    @app.route('/download_file/<img>')
    def download_file(img):
        image = os.path.join(app.config["IMAGE_UPLOADS"], img)
        return send_file(image, as_attachment=True) 

    return app