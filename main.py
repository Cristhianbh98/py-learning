import re

def is_email_valid(email: str) -> bool:
  m = re.search('^[A-Za-z0-9.]+@[A-Za-z0-9.]+\.[A-Za-z0-9]{2,3}$', email)
  return bool(m)

def __init__():
  email = input('Enter a email\n')
  if(is_email_valid(email.strip())):
    print(email + ' is a valid email')
  else:
    print(email + ' is not a valid email')

__init__()