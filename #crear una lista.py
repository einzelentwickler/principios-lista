#crear una lista
lista_numeros = [8, -2, 10 ,6, 7]
lista_cadenas = ["hola", "como", "estas"]

#si voy a imprimir enviando un argumento
#dentro de la lista, recurde que es EL INDICE
print (lista_numeros)

#para agregar un elemento a la lista
#debere utilizar el metodo append
num1 = int(input("ingrese un numero"))
lista_numeros.append(num1)
print(lista_numeros)

#eliminar elemento de una lista desde su valor
lista_numeros.remove(10)

#eliminar elementos de una lista desde su indice
lista_numeros.pop(0)
print (lista_numeros)
#eliminar ultimo elemento
lista_numeros.pop()
print(lista_numeros)

#ordenar elementos de una lista acsendente
lista_numeros.sort()
print(lista_numeros)

#ordenar elementos de una lista desendente
lista_numeros.sort(reserve = True)
print(lista_numeros)
lista_cadenas.sort(reserve = True)
print(lista_cadenas)

print(len(lista_numeros))

lista_numeros.clear()
print(lista_numeros[2])