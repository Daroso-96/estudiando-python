def miFuncion():
    print('¡Mi primera función!')
miFuncion()

def imprimeDato(*nombre):
    print('El nombre  es ', nombre)

#imprimeDato('Sashita', 'lalala', 'lorito')
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)
#nombreCompleto(nombre= 'Sashita', apellido= 'Dog')
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto(nombre= 'Sashita', apellido= 'Dog')
def miFuncion2(argumento = 'Sashita'):
  print(argumento)
#miFuncion2('Batman')
#miFuncion2()

def miFuncionLista(lista): 
    for el in lista:
        print(el)
#miFuncionLista(['Sashita', 'Dog'])

def concatenaNombres(lista): 
   i = ''
   for el in lista:
       i = i + el + ' '
       return i
nombres = concatenaNombres(['Sashita', 'feliz'])
print(nombres)

def recursion(i):
    if(i < 1):
      return i
        print(i)
        recursion(i - 1)
recursion(6)

