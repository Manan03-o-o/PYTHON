with open("numbers.txt") as f:
    nums = list(map(int, f.read().split()))

nums.sort()

with open("sorted.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")
print("Numbers sorted and written to sorted.txt")
print("Original numbers:", nums)
print("Sorted numbers:", nums)





