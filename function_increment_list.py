def increment_all(lista):
    result = []
    for dato in lista:
        result.append(dato + 1)
        print(result)
    return result

lista_1 = [1,2,3,4] 
print(increment_all(lista_1))
    