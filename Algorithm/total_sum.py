# Total Sum Program in Python

n = int(input("How many numbers do you want to add? "))

nums = []
print(f"Enter {n} numbers:")
for i in range(n):
    num = int(input())
    nums.append(num)

total = sum(nums)
print("Total Sum is:", total)
