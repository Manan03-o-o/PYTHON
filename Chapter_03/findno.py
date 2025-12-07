arr = list(map(int, input("Enter numbers: ").split()))

first = second = float("-inf")

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second Largest =", second)
# Find the second largest number in a list of numbers provided by the user.
# If there is no second largest number, it will print -inf.
# Example Input: 10 20 4 45 99
# Example Output: Second Largest = 45
# Example Input: 10 10 10
# Example Output: Second Largest = -inf

# Example Input: 5 3 8 6 2
# Example Output: Second Largest = 6
#
# Example Input: 1
# Example Output: Second Largest = -inf

