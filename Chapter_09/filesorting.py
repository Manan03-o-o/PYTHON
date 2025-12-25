with open("numbers.txt") as f:
    nums = list(map(int, f.read().split()))

nums.sort()

with open("sorted.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")
