from time import sleep

def fibo_gen(max = None):
    n1 = 0
    n2 = 1
    counter = 0

    if max == None:
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
    else:
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                if max < aux:
                    break
                n1, n2 = n2, aux
                counter += 1
                yield aux


fibogen = fibo_gen()

for element in fibogen:
    print(element)
    sleep(1)

