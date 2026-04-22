
def is_prime(num):
        if num <=1:
            return False
        else:
            for i in range (2, (int(num ** 0.5)) + 1 ):
                if num % i == 0:
                    return False
            return True


range_start = int(input("Please enter the start range: "))
range_end = int(input("Please enter the end range: "))

with open ("output_primes.txt", "w") as f:
    for number in range(range_start,range_end +1):
        if is_prime(number):
            f.write(f"{number}\n")
    f.close()

print("\nCheck the output_primes.txt file!")

