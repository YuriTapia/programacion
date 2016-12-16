#Yoritzkiri Tapia Mateo
#Laboratorio 3
#Ejercicio 6
print "ingresa numero de años persona"
A= float(raw_input())
def convierte(A):
    if 0 <= A <=2:
            A=  A*10.5
            return A
    if A >2:
            x= (A-2)*4+2*10.5
            return A
A= convierte (A)
if A>=0:
        print "el numero de años perro aquivalente es:",A," años perro"
elif a<0:
        print "ERROR!: no se admiten años negativos"
