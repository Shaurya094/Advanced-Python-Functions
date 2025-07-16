
numbers = input("Enter numbers seperated by commas: ")
num_list = numbers.split(',')
print("\nResults")
for num_str in num_list:
    num_str = num_str.strip()
    if not num_str.isdigit() and not (num_str.startswith('-') and  num_str[1:].isdigit()):
        print(f"{num_str} is not a valid integer")
        continue
    num = int(num_str)
    if num % 2!= 0:
        print(f"{num} is odd")
    else:
        print(f"{num} is not odd")