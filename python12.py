x=int(input("enter any number:"))
match x:
    case 0:
        print("x is zero")
    case 3:
        print("x is three")    
    case 5:
        print("x is five")
    case _ if x!= 90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)