nums_rep = [1, 2, 2, 3, 4, 4, 4, 5]
nums = []

for i in nums_rep:
    if i not in nums:
        nums.append(i)

print(nums)

