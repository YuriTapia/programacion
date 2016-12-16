#Yoritzkiri Tapia Mateo
#Laboratorio 3
#Ejercicio 3
print "ingresa primer numero"
a= int(raw_input())
print "ingresa segundo numero"
b= int(raw_input())
print "ingresa tercer numero"
c= int(raw_input())
print "numero ordenados de menor a mayor son:"
if a >= b >= c:
    print c,b,a
elif a >= c >= b:
    print b,c,a
elif b >= a >= c:
    print c,a,b
elif c >= a >= b:
    print b,c,a
elif c >= b >= a:
    print a,b,c
