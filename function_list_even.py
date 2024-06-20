def list_even(lista):
    resultado =[]
    for dato in lista:
        if dato%2== 0:
            resultado.append(dato)
            print(dato)
        print(resultado)
    return (resultado)

print(list_even([1,2,3,4,5,6,7,8,9,10,11]))
    