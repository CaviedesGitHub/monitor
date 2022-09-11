from flaskr import create_app
from flask_restful import Api
import requests
import time
from datetime import datetime

app=create_app('default')
app_context=app.app_context()
app_context.push()


api = Api(app)
#api.add_resource(VistaLogIn, '/login')

uri='http://127.0.0.1:5000/ping'
contador=0
while True:
    inicio=time.time()
    data=requests.get(uri)
    fin=time.time()
    if data.status_code==200:
        if fin-inicio>1:
            contador=contador+1
            with open('demoras_pingpong','a+') as file:
                file.write('{} Tiempo Superado en PingEcho: {} el {}\n'.format(contador, fin-inicio, datetime.utcnow()))
    else:
        with open('demoras_pingpong','a+') as file:
                file.write('SERVIDOR CAIDO\n')
    time.sleep(3)


#if data.status_code==200:
#data=requests.get(uri)#if data.status_code==200:
#    data=data.json()
#    print(data)

