def decorador(func):
    def envoltura(texto):
        return print(func(texto).upper())
    return envoltura

@decorador
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

if __name__ == '__main__':
    mensaje("Jeisson")

#print(mensaje("Jeisson"))
