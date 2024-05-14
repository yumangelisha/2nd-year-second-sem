power=float(input("Enter the power to input:"))
digits=int(input("Enter the number of digits:"))

answer=2**power
number=answer % (10**digits)
print(number)

