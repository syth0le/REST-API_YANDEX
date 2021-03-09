import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db.init_app(app)
#
# with app.app_context():
#     db.create_all()
#
# ma = Marshmallow(app)
# migrate = Migrate(app, db)
########################



# import connexion
#
# app = connexion.FlaskApp(__name__, specification_dir='openapi/')
# app.add_api('openapi.yaml')
# app.run(port=8080)

# import connexion
#
# app = connexion.FlaskApp(__name__, specification_dir='./')
#
# app.add_api('openapi.yaml', strict_validation=True, resolver=connexion.resolver.RestyResolver('api'))
#
#
# if __name__ == '__main__':
#     app = app.app.create_connexion_app()
#     app.run(host='0.0.0.0', port=5000, debug=True)
