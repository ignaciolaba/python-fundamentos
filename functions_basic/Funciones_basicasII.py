# 1
def countdown(x):
    for x in range(x, -1, -1):
        print(x)

countdown(5)

#2
def imprimir_y_devolver(x,y):
    print(x)
    return(y)

imprimir_y_devolver(1,2)

#3

def primer_mas_longitud(a):
    b = a[0]
    d = len(a)
    print( b + d )
    return b + d

a = [1,2,3,4,5]
primer_mas_longitud(a)

#4
def valores_mayores_que_el_segundo(h):
    k = h[1]
    for i in range(0, len(h), 1):
        if(h[i]>k):
            print(h[i])


h = [1,3,5,1,3,5,6,7]
valores_mayores_que_el_segundo(h)

#5

def length_and_value(a,b):
    length = a
    value = b 
    arr = []
    while(len(arr)<a):
        arr.append(b)
    print(arr)
    return arr

length_and_value(4,7) 