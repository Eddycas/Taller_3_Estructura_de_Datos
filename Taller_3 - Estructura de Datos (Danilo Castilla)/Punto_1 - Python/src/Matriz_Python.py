'''
Created on 26 nov. 2017

@author: Danicas99
'''
import random #import library

matriz = []

filas = int(input("Tamano del arreglo: \n")) #Method that forms a rhombus and prints its elements
columnas = filas

for f in range(0,filas):
    matriz.append([0]*columnas)
    
for f in range(0,filas):
    for c in range(0,filas):
        matriz[f][c] = random.randint(1,9)
    #print()
    
for f in matriz:
    for c in f:
        print(c,end=" ")
    print("")
print()
    
mt = (filas//2)

if filas%2 != 0: #Conditions for printing the inside of the Rhombus
     
    for f in range(0,filas):
        for c in range(0,filas):
            if (f+c>=(mt) and f+(mt)>= c and c+(mt)>= f and f+c<=(mt)+filas-1):
                print(matriz[f][c],end=" ")
            else:
                matriz[f][c] = " "
                print(matriz[f][c],end=" ")
        print("")              
else:
    for f in range(0,filas):
        for c in range(0,filas):
            if (f+c>=(mt)-1 and f+(mt)>= c and c+(mt)>= f and f+c<=(mt)+filas-1):
                print(matriz[f][c],end=" ")
            else:
                matriz[f][c] = " "
                print(matriz[f][c],end=" ")
        print("") 