prime-numbers.p# Python program to display all the prime numbers within an interval


LowerLimit = 1
UpperLimit = 250

#Print statement 
print("Prime numbers between", LowerLimit, "and", UpperLimit, "are:")

#For loop to use a counter to run through all the numbers within the range LowerLimit, UpperLimit. 
#Need to include +1 because indexing starts at 0 so if you want the UpperLimit variable to 250 you have to use +1.  

for num in range(LowerLimit, UpperLimit + 1):
   # all prime numbers must be greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


