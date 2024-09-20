from datetime import date
from typing import Self

class Person:
   def __init__(self, name: str, age: int):
      self.name = name
      self.age = age
      
   def description(self) -> str:
      return f"{self.name} is {self.age} years old"
   
   @classmethod
   def age_from_year(cls, name: str, birth_year: int) -> Self:
      current_year: int = date.today().year
      age: int = current_year - birth_year
      return cls(name, age)
   
   
if __name__ == "__main__":
   federico = Person.age_from_year("Federico", 1997)
   print(federico.description())