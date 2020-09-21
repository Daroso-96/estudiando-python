if 5 > 3:
    print('5 es mayor que 3')


x = 5    
y = 'Sashita feliz'
#print(x,y)
email = 'sashita@feliz.com'
#print(email)
inicio = 'Hola'
final = 'mundo'
#print(inicio + final)
palabra = 'Hola mundo'
oracion = "Hola mundo con comillas dobles"
 
lista = [1,2,3]
lista2 = lista.copy()
lista.append('Sashita feliz jugando ')
print(lista, lista2.count(5))
print(len(lista)) 
lista.pop()
lista.reverse()
lista.sort()
tupla = ('Hola', 'mundo', 'somos', 'tuplas')
listaDeTupla = list(tupla)
listaDeTupla.append('Sashita')
print(listaDeTupla)
rango = range(6)
#print(rango)
diccionario = {
    "nombre": "Sashita",
    "raza ":  "Weimaraner",
    "edad" : 1
}

diccionario['nombre'] = 'Lucerito'
#print(len(diccionario))
diccionario['Ladra'] = 'si'
#diccionario.popitem()
copiaPerrito = diccionario.copy()
del diccionario['Ladra']
#print(diccionario)
diccionario.pop('edad')
#print(diccionario, copiaPerrito)
perritos = {
    "sashita" : {
        "nombre": "sashita",
        "edad": 1
    },
    "lucerito" : {
        "nombre": "lucerito",
        "edad" : 2

    }
}
print(perritos)
gatitos = dict(nombre = "Agatha" , edad = 1)
print(gatitos)

verdadero = True 
falso = False 
print(verdadero, falso)