a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(f"Before swapping:")
print(f"first number=", a)
print(f"second number=", b)

a,b = b,a

print(f"After swapping:")
print(f"first number=", a)
print(f"second number=", b)