## Lamda map and filter

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# option 1

my_nums_squared = [square(num) for num in my_nums]
print(my_nums_squared)

## Map example
# alternatively use map function
a = list(map(square, my_nums))
print(a)


## Filter example
# leverage functions that return a boolean expression to filter a list
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
print(list(filter(check_even,my_nums)))

## Lamda function
# the map function accepts a defined function, but this takes up a lot space. If you have a one off function you won't use again, then use lamda.
print(list(map(lambda num: num**2, my_nums)))