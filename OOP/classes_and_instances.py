class Employee:
   def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + "." + last +"@company.com"
      
   def fullname(self):
      return "{} {}".format(self.first, self.last)
   
   
emp_1 = Employee("Corey", "Trump", 4000)
emp_1 = Employee("User", "Test", 6500)