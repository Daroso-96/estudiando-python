dato = input('Ingrese dato: ')
print(dato)
lista = ['Hola', 'Sashita', 'bonita', 'perritos']
if lista.count(dato) > 0:
    print('El dato existe:' , dato)
else:
    print('El dato no existe', dato)



primero = input('Ingrese primer número: ')
try:
    primero = int(primero)
except:
    primero = 'Sashita feliz'

if primero == 'Sashita feliz':
    print('El valor ingresado no es entero')
    exit()
segundo = input('Ingrese segundo número: ')

try:
   segundo = int(segundo)
except:
    segundo = 'Sashita feliz'
    
if segundo == 'Sashita feliz':
    print('El valor ingresado no es entero')
    exit()

#if primero == 'Sashita feliz' or segundo == 'Sashita feliz':
   # print('Ingresaste mal un dato, prueba de nuevo con solo números')
simbolo = input('Ingrese operación: ')
if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
     print('Resta: ', primero - segundo)
elif simbolo == '*':
     print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
     print('Division: ', primero / segundo)
else: 
    print('El simbolo ingresado no es valido')



