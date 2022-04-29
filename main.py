from typing import List
from Car import Car
import re

def is_email_valid(email: str) -> bool:
  m = re.search('^[A-Za-z0-9.]+@[A-Za-z0-9.]+\.[A-Za-z0-9]{2,3}$', email)
  return bool(m)

def __init__():
  # Regex
  # email = input('Enter a email\n')
  email = 'cristhian@bacusoy.com'
  if(is_email_valid(email.strip())):
    print(email + ' is a valid email')
  else:
    print(email + ' is not a valid email')

  # Class
  toyota = Car('Toyota', 'Red', 5)
  toyota.add_passengers('Cristhian')
  toyota.add_passengers('Diego')
  print(toyota.passengers)  

  # List
  fruits = ['Apple', 'Watermelon', 'Melon']
  print('Original List: ', fruits)
  # add new item to the list
  fruits.append('Grapes')
  print('Grapes added: ', fruits)
  # Count the given argument in the list
  print('Amount of apples: ', fruits.count('Apple'))
  print('Length: ', len(fruits) )
  fruits.reverse()
  print('List reversed: ', fruits)
  #reverse the list
  # clear all the items of the list
  fruits.clear()
  print('List cleared', fruits)

__init__()