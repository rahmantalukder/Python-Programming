# তিনটি সংখার মধ্যে ছোট সংখা বের কর
import math
a = int(input("Enter Fast Number: "))
b = int(input("Second Number: "))
c = int(input("Enter Third Number: "))
if(a <= b) and (a <= c):
    print("Small number is a:", a)
elif(b <= a) and (b <= c):
    print("Small number is b:", b)

else:
    print("Small number is c:", c)
    
