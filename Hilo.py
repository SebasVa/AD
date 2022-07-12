import threading
import time
import datetime
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')

#En el siguiente ejemplo de hilos se va a simular un proceso pesado de hilos
#Al ejecutar el metodo se ejecutan simultaneamente consultar y guardar
def consultar(id_persona):
    logging.debug("Consultando para el id " + str(id_persona))
    time.sleep(2)
    return


def guardar(id_persona, data):
    logging.info("Guardando para el id " + str(id_persona) + " la data " + data)
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()

#crear unas variable con el modulo thread con las funciones de consultar y guardar
t1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "Prueba AD" ))

#El consultar y guardar deben demorar un tiempo para que simule el proceso

t1.start()
t2.start()
# consultar(1)
# guardar(1, "Prueba AD" )

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second))