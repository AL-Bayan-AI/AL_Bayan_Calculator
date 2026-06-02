#Albayan Apps 

print("Welcome to the AL bayan Apps\nWe're here to help you with math,Specifically divison, multiplication,Addition,and Subtraction Note : The project developer dose note permit the app to be copied without thir knowledge.")
print("__________________________________________________________")

name=str(input("Enter your name : "))
print("Welcome to Al bayan Apps : " +str(name))
num1=float(input("Enter First Number  : "))
oper=input("Chose an operation (+.-.*./.%) : ")
num2=float(input("Enter Sec Number : "))

if oper=="+":
    result=num1+num2
    print(num1,"+" ,num2, "= ",result)
    
elif oper=="-":
    resuit=num1-num2
    print(num1,"-" ,num2, "= ",result)
    
elif oper=="*":
    result=num1*num2
    print(num1,"*",num2, "= ",result)
elif oper=="/":
  if num2 != 0:
    result=num1/num2
    print(num1,"/" ,num2, "= ",result)
  else:
      print("Can t Division by Zero")
      
elif oper=="%":
    result=num1%num2
    print(num1,"%" ,num2, "= ",result)
    
print("Good?")
say=input()
print("ok is your like this? while say : " +str(say))
say2=str(input())
print("IF you encounter a problem, you can inquire via the email address below\n email : contact.bayanfd@gmail.com\n Send your experience via email.\n YA  :  " + str(name))
#finaly, you can inquir about anything related to this project :
#contact.bayanfd@gmail.com


    
