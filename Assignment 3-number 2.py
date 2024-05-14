#Program to print the first n Fibonacci numbers

#Ask the user for the number to print
num=int(input("How many Fibonacci numbers would you want to print?:"))

#initialize the first two numbers of the sequence
a=0
b=1

#Print the first n Fibonacci numbers
for i in range(num):
    print(b)
    temp=a
    a=b
    b=temp+b