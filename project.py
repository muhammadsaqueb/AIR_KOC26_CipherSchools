n=True
import math
while (n):
    n=n+1
    print("""Press 
    {'S' or 's'}---FOR START
    {'E' or 'e'}---FOR EXIST
    """)
    en=str(input('Enter your Choice---'))
    if en=="S" or en=="s":
        print(""" 
            Press -  
            0 - Addition(x, y) 
            1 - Subtraction(x,y) 
            2-  Multiplication(x,y) 
            3 - Division(x, y) 
            4  - Modulus (%)
            5- Exponent(x, y) 
            6 - tan(x, y) 
            7 - sin(x) 
            8 - cos(x) 
            9 - Radian to Degree 
            10 - Degree to Radian
            """)
        num= input("Enter Your Choice=") 
        if num== "0":
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(x + y) 
        elif num == "1": 
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(x-y) 
        elif num == "2": 
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(x*y) 
        elif num== "3": 
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(x/y) 
        elif num=="4":
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(x % y) 
        elif num == "5": 
            x = float(input("Your number -")) 
            y = float(input("Power -")) 
            print(x**y) 
        elif num == "6": 
            x = float(input("1st number -")) 
            y = float(input("2nd number -")) 
            print(math.tan(x)) 
        elif num == "7": 
            x = float(input("Enter your number=")) 
            print(math.sin(x)) 
        elif num== "8": 
            x = float(input("Enter your number=")) 
            print(math.cos(x))
        elif num == "9": 
            x = float(input("Enter your number=")) 
            print(math.degrees(x))
        elif num == "10": 
            x = float(input("Enter your number=")) 
            print(math.radians(x))
    elif en=="E" or en=="e":
        break
    else:
        print("INVALID")