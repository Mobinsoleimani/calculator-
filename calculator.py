x=int (input("add your num :"))
sign=input("chois the sign (+,//,-,*) :")
y=int (input("add your num :"))

def calculator():
   

    if sign=="+":
        t = x + y
    elif sign=="-":
        t = x - y
    elif sign=="*":
        t = x * y
    elif sign=="//":
        t = x // y   
    else:
        print("Invalid sign")
        return
    print(t)
        
    
calculator()