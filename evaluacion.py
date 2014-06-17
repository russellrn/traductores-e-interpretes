# russell hasson C.I 20.586.842


def funcion_suma(a=0,b=0):
    print "el resultado de la suma es:", int(a)+int(b)

def funcion_resta(a=0,b=0):
    print "el resultado de la resta es:", int(a)-int(b)

def funcion_multiplicar(a=1,b=0):
    print "el resultado de la multiplicacion es:", int(a)*int(b)

def funcion_dividir(a=0,b=1):
    print "el resultado de la division es:", int(a)/int(b)

def funcion_exponente(a=1,b=0):
    print "el resultado es", int(a)**int(b)

def funcion_raiz(a):
    import math
    raiz=math.sqrt(a)
    print "la raiz cuadrada es: ", raiz

print "  INGRESE:\ns para suma \nr para resta \nm para multiplicar \nd para dividir \ne para exponente\nz para raiz cuadrada"

x=raw_input ("ingrese la letra de la operacion que desea realizar: ")


if x == "s":
    a=raw_input ("ingrese primer valor: ")
    b=raw_input ("ingrese segundo valor: ")
    funcion_suma(a,b)
elif x == "r":
    a=raw_input ("ingrese primer valor: ")
    b=raw_input ("ingrese segundo valor: ")
    funcion_resta(a,b)
elif x == "m":
    a=raw_input ("ingrese primer valor: ")
    b=raw_input ("ingrese segundo valor: ")
    funcion_multiplicar(a,b)
elif x == "d":
    a=raw_input ("ingrese primer valor: ")
    b=raw_input ("ingrese segundo valor: ")
    funcion_dividir(a,b)
elif x == "e":
    a=raw_input ("ingrese primer valor: ")
    b=raw_input ("ingrese segundo valor: ")
    funcion_exponente(a,b)
elif x == "z":
    a=input("Ingrese numero a sacar su raiz cuadrada: ")
    funcion_raiz(a)
