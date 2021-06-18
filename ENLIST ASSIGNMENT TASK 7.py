#Create a function getting two integer inputs from user
def mylist():
    a = int(input("enter the first number="))
    b = int(input("enter the second number="))
    x = a+b
    print("the addition of the two integer numbers=",x)
    x = a-b
    print("the subtraction of two integer numbers=",x)
    x = a*b
    print("the multilplication of two integer numbers=",x)
    x = a/b
    print("the division of two integer numbers=",x)
mylist()

#add ,sub
def sandy(x,y):
    c = x+y
    d = x-y
    a = x*y
    b = x/y
    return c,d,a,b
result1,result2,result3,result4 = sandy(10,2)
print(result1,'\n',result2,'\n',result3,'\n',result4,'\n')

#function covid
x = input("enter the covid patient name:")
x = 98
if(x!=98):
    print("enter the body temperature:",numb)
else:
    print("the body temp is = 98")