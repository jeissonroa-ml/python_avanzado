from time import sleep

def fibo_gen(max = None):
    n1 = 0
    n2 = 1

    if max == None:
        while True:
            yield n1
            n1, n2 = n2, n1+n2
    else:
        while n1 <= max:
            yield n1
            n1, n2 = n2, n1+n2


fibogen = fibo_gen(21)

for element in fibogen:
    print(element)
    sleep(1)

