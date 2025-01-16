#Prompt the user for the length and width of a rectangle.
#Calculate and display the area using the input values. Use “float” data type to represent all values.

Length = float(input("Enter length: "))
Width = float(input("Enter width: "))
Area = float(Length * Width)
print(f"The Area is: {Area:.2f}")
