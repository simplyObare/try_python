from datetime import date
from typing import Self

class Calculator:
   def __init__(self, version: int) -> None:
      self.version = version
      
   def description(self):
      print(f"Currently running Calculator on version: {self.version}")
      
   @staticmethod
   def add_numbers(*numbers: float) -> float:
      return sum(numbers)
      
      
if __name__ == "__main__":
   cal_1 = Calculator(10)
   cal_2 = Calculator(200)
   
cal_1.description()
cal_2.description()


print(Calculator.add_numbers(1,3,4))