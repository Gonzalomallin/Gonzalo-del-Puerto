def es_par(a, b):
    return a + b

sumarI = es_par(5, 6)

if(sumarI % 2 == 0):
    print("TrueI")
else:
    print("FalseI")

sumarII = es_par(5, 5)

if(sumarII % 2 == 0):
    print("TrueII")
else:
    print("FalseII")

sumarIII = es_par(4, 102)

if(sumarIII % 2 == 0):
    print("TrueIII")
else:
    print("FalseIII")
print(f"El resultado es {sumarI}")
print(f"El resultado es {sumarII}")
print(f"El resultado es {sumarIII}")










