def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
     return"error division by zero"
    return x/y
def calculator():
   print("select operation")
   print("1.Add")
   print("2.subtract")
   print("3.multiply")
   print("divide")
choice=input("enter choice(1/2/3/4):")
if choice in['1','2','3','4']:
   num1=float(input("enter first number"))
   num2=float(input("enter second number"))
   if choice=='1':
    print(f"{num1}={num2}+(add(num1,num2))")
   elif choice=='2':
    print(f"{num1}-{num2}+(subtract(num1,num2))")
   elif choice=='3':
    print(f"{num1}*{num2}=(multply(num1,num3))")
   elif choice=='4':
    print(f"{num1}/{num2}=(divide(num1,num2))")
   else:
    print("invalid input")
   if __name__=="__main__":
      calculator()