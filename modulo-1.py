from  modulos import saludo , mascotas
from camelcase import CamelCase
print(mascotas)
saludo('Dayana')
c = CamelCase()
s = 'Esta oracion necesita Camel case'
camelcased = c.hump(s)
print(camelcased)