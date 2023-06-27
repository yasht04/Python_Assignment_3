i = "1"
while i == "1":
    a=int(input("Enter first Value: "))
    b=int(input("Enter Second Value: "))
    print("\n1)Addition \n2)Subtraction \n3)Multiplication \n4)Division")
    n = int(input("Enter Choice: "))
    if n == 1:
        print("Addition:",a+b)
    elif n == 2:
        print("Subtraction:",a-b)
    elif n == 3:
        print("Multiplication:",a*b)
    elif n == 4:
        print("Quetient:",a/b)
        print("Remainder:",a%b)
    else:
        print("Invalid Choice!")
    i = input("To continue press 1 or press enter to exit ")
    if i != "1":
        exit()   