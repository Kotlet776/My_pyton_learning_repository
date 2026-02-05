#4.1 if
i = 3
if i == 2:
    print(f"{i} is eaqual to two")
elif i == 3:
    print(f"{i} is eaqual to three") # this will be printed
else:
    print(f"{i} is neither equal to two or three")

#4.2 for
l = ["apple", "banana", "carrot", "mango"]
for i in l:
    print(i) # the items in the list will be printed in sequence from first to last in different rows

#4.3 range()
for x in range(2, 15, 2):
    print(x) # numbers from two to fourtheen will be printed, but with jumps of 2, so: 2, 4, 6, ..., 14

#4.4 break, continue

for i in range(1, 10):
    if i == 5:
        break # when "i" is eaqual to five this line will run and turn off the whole loop even thoug the range hasn't finished.
    elif i % 2 == 0:
        print(f"{i} is an even number") # this will be printed as long as the loop runs and when the remainder of "i" divided by two is eaqual to zero
        continue # when this runs the loop wil start the next iteratin without executing the rows under the continue (the line 27 will not be printed)
    print(f"{i} is not an equal number") 
