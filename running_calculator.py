print ("---Running Total Calculator---")
print("Enter numbers to add them up. Type 'done' to see the total.")
count=0
total= float()
while True:
    num = (input("Enter the number or 'done' to stop:"))
    if num.lower() == "done":
        break
    numbers=float(num)
    total +=numbers
    count +=1
    print(f"Current total is:{total:.1f}")
    print(f"Number of numbers:{count}")

print(f"Current total is:{total:}")
print(f"Number of participated numbers:{count}") 