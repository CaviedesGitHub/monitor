from flask_restful import Resource
from ..modelos import db, Usuario
from flask import request

import time
from celery import Celery
from datetime import datetime
import random


contador=5

celery_app=Celery(__name__, broker='redis://localhost:6379/0')
@celery_app.task(name='demora')
def demora(*args):
    pass


class VistaLogIn(Resource):
    contador=33
    lasdemoras=[0.5, 2.0, 3.2, 4.2, 1, 0.2, 0.3, 5, 1.2, 1]    
    def post(self):
        inicio=time.time()
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        indice=usuario.conteo%10                                      
        usuario.conteo=usuario.conteo+1
        db.session.commit()
        #time.sleep(random.uniform(0,5))
        time.sleep(self.lasdemoras[indice])
        fin=time.time()
        dem=fin-inicio
        self.contador=self.contador+1
        args=(indice, dem, datetime.utcnow())
        demora.apply_async(args=args)
        if usuario is None:
            return "El usuario no existe", 404
        else:
            return {"mensaje": "Login"}

class VistaPingPong(Resource):
    def get(self):
        time.sleep(random.uniform(0,2))
        return {"Echo":"Pong"}