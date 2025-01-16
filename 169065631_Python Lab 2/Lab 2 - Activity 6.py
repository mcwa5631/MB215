N1 = float(input("Enter first number: "))
N2 = float(input("Enter second number: "))

Add = float(N1 + N2)
print(Add)
Sub = float(N1 - N2)
print(Sub)
Mul = float(N1 * N2)
print(Mul)

if N1 == 0 or N2 == 0:
    Div = "N/a"
else:
    Div = float(N1 / N2)
print(Div)

if N1 == 0 or N2 ==0:
    Int = "N/a"
else:
    Int = float(N1//N2)
print(Int)


Rem = float(N1 % N2)
print(Rem)
Pow = float(N1**N2)
print(Pow)

