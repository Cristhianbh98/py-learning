""" Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. """

currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input('Introduce una moneda \n')

print(currencies.get(currency.title(), 'La moneda no se encuentra'))
