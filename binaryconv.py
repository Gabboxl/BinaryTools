while True:
    num: int = input("Inserisci un numero binario da convertire in decimale: ")

    for i in str(num):
        if i in '10':  # If digit is 1 or 0
            binary = True
        else:
            binary = False
    if not binary:
        print('Must be a binary number (contain only 1s and 0s) sucsa')
        break

    binario = list(map(int, num))
    binario.reverse()
    snumeri = []
    asd = 0
    for numero in binario:
        # if numero == 0 or numero == 1:
        snumeri.append(pow(2, asd) * numero)
        asd += 1

    print(sum(snumeri))
    print(snumeri)
    # sucsa
