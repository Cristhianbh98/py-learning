class Car:
  def __init__(self, name, color) -> None:
    self.name = name
    self.color = color
  
  def __str__(self) -> str:
    return 'Name: ' + self.name + ';Color: ' + self.color