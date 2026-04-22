"""
Write a loop that prints the multiplication of
a given number.
1) Start
2) Ask the user to enter number
3) Input number
4) Ask the user to enter limit (until what number
they want the table of multiplication)
5) Input n
6) set result to 0
7) set i to 1
8) for i <= n
calculate result as number * i
output result
increment i
end for
9) End

"""
number = int(input("Please enter number: "))
n = int(input("Please enter limit: "))
result = 0
print(f"\nMultiplication table for {number}:")
for i in range(1,11):
    result = number * i
    print(f"{number}x{i} = {result}")

##########################################
#Another way (and only up to 10 as requested)

print("-"*40)

number = int(input("Enter a number: "))
print(f"\nMultiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
