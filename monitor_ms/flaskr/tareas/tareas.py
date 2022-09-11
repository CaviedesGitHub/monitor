from celery import Celery

celery_app=Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='demora')
def demora(contador, tiempo, fecha):
    print("DEMORA")
    if tiempo>=3:
        with open('demoras_login','a+') as file:
            file.write('{} Tiempo Superado en Login: {} el {}\n'.format(contador, tiempo, fecha))