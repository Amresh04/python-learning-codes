class calculator:
    def __init__(self,n):
      self.n=n
    def square(self):
       print("square=",self.n*self.n)
    def cube(self):
       print("cube=",self.n*self.n*self.n)  
    def squareroot(self):
       print("squareroot=",(self.n**0.5))
    @staticmethod
    def greet():
       print("hello")   


a=float(input("enter the no:"))
result=calculator(a)
result.square()
result.cube()
result.squareroot()
result.greet()

