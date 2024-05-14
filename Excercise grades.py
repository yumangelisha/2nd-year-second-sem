grade=eval(input("Please type your grade:"))

##A-Outstanding
if grade>=90 and grade<=100:
    print("a is outstanding:")
    
##B-Good
elif grade>=80 and grade<=89:
    print("B is good:")
    
##C-Fair
elif grade>=70 and grade<=79:
    print("c is fair:")
    
##D-Poor
elif grade>=59 and grade<=60:
    print("d is poor")
    
##E-Failed
elif grade<=60:
    print("e is for failed")
    
else:
    print("Invalid")