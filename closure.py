def make_division_by(x):
    def divisor(y):
        assert type(x) == int, "solo puedes usar enteros"
        dividir = y/x
        return dividir
    return divisor
def run():
    dividir = make_division_by(3)
    print(dividir(18))

if __name__ == '__main__':
    run()