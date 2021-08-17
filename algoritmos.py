myNumber = 42
myName = "karen"

if(myNumber == 42):
    myNumber = myName 
    myName = str(42)

print("myNumber = " + myNumber)
print("myName = " + myName)

def numeros(a, b):
    if a<=b:
        while a<=b:
            print(a)
            a=a+1
    else:
        while b<a:
            print(b)
            b=b+1  

numeros(-52, 1066)

def beCheerful():
    pass 



lista = [1, 2, 3, 4, 5, 6]
num = 3

listamenores=[]
listamayores=[]

for i in range (len(lista)):
    if lista[i] <= num:
        listamenores.append(lista[i])
    else:
        listamayores.append(lista[i])

print(listamenores)
print(listamayores)


def getListas(lista, num):
    listamenor=[]
    listamayor=[]
    for i in lista:
        if i <= num:
            listamenor.append(i)  
        else:
            listamayor.append(i)
    return listamayor, listamenor

lista = [1,2,3,4,5,6]
num= 3
getListas(lista, num)
print(getListas(lista, num))

# Paso 3
# Crear una clase Lista que contenga lo siguiente
# 1. Tendrá dos atributos, cada uno de ellos será una lista vacía
# 2. Tendrá un método llamado getListas que recibe dos parámetros, lista y num, y que al ser llamado
# almacenará en cada uno de sus atributos la lista menor y la lista mayor

class Lista:
    lista1= []
    lista2= []
    def getListas(self, lista, num):
        for i in lista:
            if i <= num:
                self.lista1.append(i)
            else:
                self.lista2.append(i)

lista = [1, 2, 3, 4, 5, 6]
num = 3
l =Lista()
l.getListas(lista, num)
print(l.lista1)
print(l.lista2)


def factorial(num):
    x=1
    for i in range(x, num+1):
        x = x* i
    return x
print(factorial(6))


def factorialRecursiva(num):
    if num == 1:
        return 1
    return factorialRecursiva(num -1)*num
print(factorial(3))

#Crea beCheerful(). Dentro de este, la cadena console.log "¡buenos días!" Llámalo 98 veces.

message ="buenos días"
x=1
while x < 98:
    x+=1
    print(message)

#Usando FOR, imprime múltiplos de 3 de -300 a 0. Omite -3 y -6. 
def multiplos(a, b):
    x= -3
    y= -6
    if a<=b:
        while a<=b:
            if a == x or a == y:
                pass
            else:
                print(a)
                a=a+3
    else:
        while b<a:
            if b == y:
                pass
            else:
                print(b)
                b=b+3  
multiplos(-300, 0) 

#Imprime números enteros de 2000 a 5280, utilizando un WHILE.
def enteros(a, b):
        while a < b:
            a= a +1
            print(a)           
enteros(2000, 5280)
   
#Si 2 números dados representan tu mes y día de nacimiento en cualquier orden, 
#registra "¿Cómo lo supiste?", de lo contrario registra "Un día cualquiera...

def cumpleaños(a, b):
    if a == 12 and b== 5:
        print("¿Cómo lo supiste")
    else:
        print('Un día cualquiera')      
cumpleaños(12, 5)

#Escribe una función que determine si un año determinado es bisiesto. Si un año es 
#divisible por cuatro, es un año bisiesto, a menos que sea divisible por 100. 
#Sin embargo, si es divisible por 400, entonces lo es.

def bisiesto(a):
    x=1
    for i in range(x, a):
        if (i%4 == 0):
            print(i,"año bisiesto")
        else: 
            print(i,"no bisiesto")
bisiesto(1000)

