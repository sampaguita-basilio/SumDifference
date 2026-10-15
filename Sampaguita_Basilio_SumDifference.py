num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

def calculate_sum():
    global sum
    sum= num1+num2
    print(f"The sum is: {sum}")

def calculate_difference():
    global difference
    difference = num1-num2
    print(f"The difference is: {difference}")

calculate_sum()
calculate_difference()