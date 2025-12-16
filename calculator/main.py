## importing modules
import addition
import subtraction as sb
from multipication import mul
from division import div

#  main 
if __name__ == "__main__":
    print("Welcome to simple calculator")
    operations = (
        "1.Addition \n",
        "2. Subtraction \n",
        "3. Division \n", 
        "4. Multiplication \n"
    )

    print(*operations)
    choice = int(input("Select your operation:"))
    if choice == 1:
        a, b = map(int, input("enter two numbers with space: ").split())
        res = addition.add(n1 = a, n2 = b)
        print(res)
    elif choice == 2:
        a, b = map(int, input("enter two numbers with space: ").split())
        res = sb.sub(n1 = a, n2 = b)
        print(res)

    elif choice == 3:
        a, b = map(int, input("enter two numbers with space: ").split())
        res = div(n1 = a, n2 = b)
        print(res)
    elif choice == 4:
        a, b = map(int, input("enter two numbers with space: ").split())
        res = mul(n1 = a, n2 = b)
        print(res)
    else:
        print("Select correct operation ")