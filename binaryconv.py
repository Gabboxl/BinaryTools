while True:
    num = input("Inserisci un numero binario da convertire in decimale: ")
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
