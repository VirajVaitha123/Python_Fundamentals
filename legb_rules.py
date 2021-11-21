## LEGB Rule

## Python will look for variables in the following order:

# Local: Variables assigned in any way within a function
lambda num:num**2 
# Enclosed function locals: Names in the local scope of any and all enclosing functions from inner to outer
name = ' This is a global string'

def greet():
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

# Global (module): Names assigned at the top level of a module file or declared global in a def within the file
name = ' This is a global string'

def greet():
    #name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()
# Built-in (Python): Names preassigned in the built-in names module: open, range, syntax error

# finally we will look at an example that takes the global value

x = 50

def func():
    global x
    print("The value is {}".format(x))

    x = 'New Value'
    print(f'I just locally changed global x to {x}')

func()

