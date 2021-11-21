## String Formatting

name = "viraj"
location = "london"
print("Hello my name is " + name + "and I live in "+location)

# .format() method
print("This is a string and my name is {0} and I live in {1}".format(name,location))


# formatting float
result = 0.123252323
print("The result was {}".format(result))

# the 1 in 1.3, declares whitespace
print("The result was {r:1.2f}".format(r=result))

# lets try 10
print("The result was {r:10.2f}".format(r=result))

# f string formatting
print(f'Hello, my name is {name} and I live in {location}')