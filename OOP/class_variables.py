class Employee:
   
   raise_amount = 1.04
   
   def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + "." + last +"@company.com"
      
   def fullname(self):
      return "{} {}".format(self.first, self.last)
   
   def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)
   
   
emp_1 = Employee("Corey", "Trump", 4000)
emp_2 = Employee("Caro", "Hemp", 6500)