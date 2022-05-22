""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. """

name = input('Ingrese su nombre \n')
address = input('Ingrese su dirección \n')
age = input('Ingrese su edad \n')
phone_number = input('Ingrese su teléfono \n')

user = {
  name: name,
  age: age,
  address: address,
  phone_number: phone_number
}

print(user[name], 'tiene', user[age], 'años, vive en', user[address], 'y su número de teléfono es', user[phone_number])
