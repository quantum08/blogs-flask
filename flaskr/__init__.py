import os
from flask import Flask

def create_app(test_config = None):

    #create and configure the create_app

    app = Flask( __name__ , instance_relative_config = True)

    #__name__ is the name of current python module

    app.config.from_mapping(  #set default configuration app will use
        SECRET_KEY='dev',  # use by flask to keep data safe
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #DATABASE is the path where SQLite database file will be saved
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)  #ensure thet app.instance_path exist
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!  using flask'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app
