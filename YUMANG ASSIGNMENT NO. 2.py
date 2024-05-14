sinigang = int(input("Enter the price of meal : "))
adobo = int(input("Enter the percentage of your tip : "))
karne = sinigang * (adobo/100)
hatdog = sinigang + karne
print("Bill of meal : ", sinigang, "\nTotal bill : " , hatdog)
