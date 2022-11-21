import random

nums = []
numsAbove = []
for i in range(100):
    nums.append(random.randint(0, 100))

avg = int(sum(nums)/len(nums))


for i in nums:
    if i > avg:
        numsAbove.append(i)


print("The average is: ", avg)
print("Numbers above the average are: ", numsAbove)
