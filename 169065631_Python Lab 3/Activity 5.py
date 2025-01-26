count = 0
total = 0
#initializes variables

#makes sure total is less than 100
while total < 100:
    
    Number = input("Input number here or click space to end: ").strip()
    #gets number from user

    if Number == "":
        break
    #if input is space it will break the loop

    Num = float(Number) #makes inputted number become a float number 
    total += Num #adds the inputted number to the total
    count += 1 #adds 1 to the count
    print(f"Total: {total} and Count: {count}") #prints count and total

print(f"final Total: {total} and Count: {count}") #if space is entered the final count and total are displayed
