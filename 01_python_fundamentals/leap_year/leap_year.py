
"""
1) Start
2) Ask the user to enter year
3) Input year
4) Set leap to 0 (0 means not a leap year, 1 means leap year)
5) if year % 400 = 0
      then set leap to 1
   else if year % 100 = 0
      then set leap to 0
   else if year % 4 = 0
      then set leap to 1
   end if
6) if leap = 1
      then output "leap year"
   else
      output "not leap year"
   end if
7) End

"""

year = int(input("Please enter the year to check whether it is a leap year or not: "))
leap = 0

if year % 400 == 0:
    leap = 1
elif year % 100 == 0:
    leap = 0  # Not a leap year
elif year % 4 == 0:
    leap = 1

if leap == 1:
    print("The year is a leap year.")
else:
    print("The year is NOT a leap year.")

#################################################################
#Another way to do it:
print("-"*40)

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")
