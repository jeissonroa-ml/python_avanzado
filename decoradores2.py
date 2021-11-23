from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): # se ponen estos valores para que reciba cualquier valor y se puedan ejecutar diferentes funciones
        # *args = argumentos
        # **kwargs = argumentos nombrados
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func(): #función sin argumentos
    for _ in range(1, 10000000):
        pass

@execution_time
def sum(a: int, b:int) ->int: #función con argumentos
    return a + b

@execution_time
def mensaje(nombre = "Jeisson"): #función con argumentos nombrados
    return print(nombre)

random_func()
sum(2,2)
mensaje()