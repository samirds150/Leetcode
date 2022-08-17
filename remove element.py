nums = [0,1,2,2,3,0,4,2]
val = 2


list1 = []

for i in nums:
    if i != val:
        list1.append(i)
print(len(list1))