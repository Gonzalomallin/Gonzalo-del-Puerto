nums = [10, -1, 2, 3, 5, 7, 6, -10]

print("De la lista, los números par son los siguientes: ")

for i in range(len(nums)):
    if not nums[i] % 2:
        print(nums[i])

