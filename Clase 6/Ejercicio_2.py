nums = []
nums.append(1)
nums.append(100)
nums.append(300)
nums.append(1000)

suma = 0
for i in nums:
    suma = suma + i

print(f"{suma}")
print(len(nums))

cantidad_num = len(nums)
promedio_num = suma / cantidad_num

print(f"La suma es de {suma}, la cantidad de numeros es de {cantidad_num} y, el promedio, es de {promedio_num}")


