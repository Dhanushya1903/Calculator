a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
print(" 1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n")
choice = int(input("Enter the choice to perform the arithmetic operation : "))
match choice :
    case 1 :
        print("The addition of the two numbers is ",a+b)
    case 2:
        print("The subtraction of the two numbers is ",a-b)
    case 3 :
        print("The multiplication of the two numbers is ",a*b)
    case 4 :
        print("The division of the two numbers is ",a/b)
    case _ :
        print("Enter a valid choice")
