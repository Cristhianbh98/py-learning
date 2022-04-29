class Car:
  def __init__(self, name: str, color: str, length: int) -> None:
    self.name = name
    self.color = color
    self.length = length
    self.passengers = []
  
  def __str__(self) -> str:
    return 'Name: ' + self.name + ';Color: ' + self.color

  def add_passengers(self, passenger: str): 
    self.passengers.append(passenger)