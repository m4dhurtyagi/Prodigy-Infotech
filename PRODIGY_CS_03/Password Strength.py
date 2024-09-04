def complex(Text):
    length= len(Text)
    U=0
    L=0
    C=0
    N=0
    S=0
    
    for i in range(length):
        ch = Text[i]

        if ch == " ":
            continue
        elif (ch.isupper()):
            U = 1
        elif (ch.islower()):
            L=1 
        elif (ch.isnumeric()):
            N=1
        else:
            C=1
    
    if U == 0:
        print("Add An Upper Case")
    else:
        S+=20
    if L == 0:
        print("Add A Lower Case")
    else:
        S+=20
    if C == 0:
        print("Add A Special Character")
    else:
        S+=20
    if N == 0:
        print("Add A Number")
    else:
        S+=20
    if length < 8:
        print("Create A Longer Password")
    else:
        S+=20
    
    print("PASSWORD STRENGTH : ",  S , "%")

def main():
    print(30*"=" + "PASSWORD ANALYZER" + 30*"=")
    Text = input("Enter Password : ")
    print("RESULTS : ")
    complex(Text)

while True:
    main()