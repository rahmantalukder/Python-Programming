# তিনটি সংখার মধ্যে বড় সংখা বের কর
import math
a = int(input("Enter Fast Number: "))
b = int(input("Second Number: "))
c = int(input("Enter Third Number: "))
if(a >= b) and (a >= c):
    print("Largest number is a:", a)
elif(b >= a) and (b >= c):
    print("Largest number is b:", b)

else:
    print("Largest number is c:", c)

