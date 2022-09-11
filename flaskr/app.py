from flaskr import create_app
from flaskr.vistas.vistas import VistaPingPong
from .modelos import db
from flask_restful import Api
from .vistas import VistaLogIn

app=create_app('default')
app_context=app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaPingPong, '/ping')