# Python program to display all the prime numbers within an interval

firstnumber = 1
lastnumber = 250

print("Prime numbers between", firstnumber, "and", lastnumber, "are:")

for num in range(firstnumber, lastnumber + 1):
   # all prime numbers are 1 or greater than 1
   if num >= 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


