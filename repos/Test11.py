# num=int(input())
# print(num)
# decimalnum=input()
# decimalnum=float(input())
# print(decimalnum)

# #give two integers in first line and more than two integers in third line
# a, b = map(int, input().split())
# array = list(map(int, input().split()))
# sum = 0
# for each in array:
#     sum = sum + each
# print(a, b, sum)  # prints first two integers from first line and sum of integers of second

# a = 5
# b = 0.63
# c = "hello"
# print("a is : %d, b is %.4f,c is %s" % (a,b,c))

# # Taking the name input using input()
# name = input("Enter your name: ")

# # Taking the age input using input() and converting it to integer
# age = int(input("Enter your age: "))

# # Taking the country input using input()
# country = input("Enter your country: ")

# # Displaying the formatted sentence with name, age, and country
# print("Hello, my name is %s, I am %d years old, and I am from %s." %(name, age, country))

# import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)

# for random_number in lottery():
#        print("And the next number is... %d!" %(random_number))

# squares = (x*x for x in range(5))
# for val in squares:
#     print(val)


def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1, 2, 3, 4, 5)

def greet(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

greet(name="Hữu", age=19, school="HCMUS")
