
tipo1 = input()

if tipo1 == 'i':
    obj_int1 = int(input())
else:
    obj_float1 = float(input())

tipo2 = input()

if tipo2 == 'i':
    obj_int2 = int(input())
else:
    obj_float2 = float(input())

# Casos

# Caso 1: int + int
if tipo1 == 'i' and tipo2 == 'i':
    print(obj_int1 + obj_int2)
    
# Caso 2: float + int
elif tipo1 == 'f' and tipo2 == 'i':
    print(format(obj_float1 + obj_int2, ".2f"))
    
# Caso 2: int + float
elif tipo1 == 'i' and tipo2 == 'f':
    print(format(obj_int1 + obj_float2, ".2f"))
    
# Caso 3: float + float
else:
    print(format(obj_float1 + obj_float2, ".2f"))
