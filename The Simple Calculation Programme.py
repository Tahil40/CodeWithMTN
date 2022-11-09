print("Enter The First number; ")
try:
    n1 = int(input())
except Exception as e:
    print(e)
    n1 = int(input("Please Enter Number Again in Number Format; "))

print("Enter The Second Number; ")
try:
    n2 = int(input())
except Exception as e:
    print(e)
    n1 = int(input("Please Enter Number Again in Number Format; "))

print("Choose from the given expression; (+) (-) (*) (/)")
n3 = input()

if n3=="+":
    add = (n1+n2)
    print("The Sum of '"+str(n1)+"' and '"+str(n2)+"'; ", add)

if n3=="*":
    nul = (n1*n2)
    print("The Multiplication of '" +str(n1)+ "' and '" +str(n2)+ "'; ", nul)

if n3=="-":
    minus = (n1-n2)
    print("The Subtraction of '" +str(n1)+ "' and '" +str(n2)+ "'; ", minus)

if n3=="/":
    div = (n1/n2)
    print("The Division of '" +str(n1)+ "' and '" +str(n2)+ "'; ", div)

if n3 not in [("+"), ("-"), ("/"), ("*")]:
    print("Error: Somethig wrong, Please Enter use Correct Mathematical Expression")