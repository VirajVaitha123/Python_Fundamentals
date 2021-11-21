## Tuples

# create tuple
t = (1,1,2,3)

# check length
print(len(t))

# retrieve values with index position
print(t[0])
print(t[-1])

# tuples can't be reassigned
print("Next line of code will fail to show tuples are immutable")
t[0] = 2