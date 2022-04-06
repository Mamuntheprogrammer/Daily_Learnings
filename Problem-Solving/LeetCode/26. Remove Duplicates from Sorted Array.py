nums=[1,1,2]

s = set(nums)

nums[:len(s)] = sorted(s)

print(nums)

k = len(s)

print(k)
        