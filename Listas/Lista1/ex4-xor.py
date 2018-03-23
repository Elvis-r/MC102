# Swap without aux using ^(XOR)

x = input()
y = input()

x = int(x)
y = int(y)

print("x: ", x)
print("y: ", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After swapping:")
print("x: ", x)
print("y: ", y)

