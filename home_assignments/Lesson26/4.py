numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
