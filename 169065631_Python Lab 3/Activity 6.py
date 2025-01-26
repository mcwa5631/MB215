print("Even numbers from 2 to 20:") #prints out even numbers starting from 2 going to 20
for num in range(2, 21, 2): #starts at number 2 and ends before 21 going up by 2 each time
    print(num, end=" ") #prints the numbers and ends each one with a space for visibility

print("multiplication table for numbers 1 to 3:") 
for i in range(1, 4): #iterates through 1,2,3
    for j in range(1, 11):#iterates through 1 to 10 (stops before 11)
        print(f"{i} * {j} = {i * j}")#multiples the numbers out from 1, 2, and 3 
    print()

string = "Hello" #sets string equal to Hello
print("\n'Hello' reversed:") #creates new line and says Hello will be reversed
for char in reversed(string):
    print(char, end=" ") #revereses the wolrd hello by printing each letter first then adding a space until whole word is printed
