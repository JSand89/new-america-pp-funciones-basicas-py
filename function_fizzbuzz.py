def list_even(lista):
    for dato in lista:
        if dato%3== 0 and dato %5 ==0:
            print("fizzbuzz",dato)
        elif dato %3 == 0:
            print("fizz",dato)
        elif dato %5 == 0:
            print("buzz",dato)
    return 

list_even([1,2,3,4,5,6,7,8,9,10,15,30])
    