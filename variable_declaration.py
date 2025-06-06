# To define variables in python it is enough to pick a name for your variable and assign it a value
# Like so:

my_var = 0

# Where you declare your variable decides where it can be accessed from and when it will be freed from memory
# For example if you define your variable inside a function, when the function exists, that memory will be freed

def my_function():
    my_second_var = 1

    # This works
    print(my_second_var)

# This does not
# print(my_second_var)

# We call the "place" in the code where a variable can be accessed its "scope"
# In python, a scope can be a nesting level under an if, for, while, with, etc
# Or a class, or function, OR namespace* (elements in a namespace can be accessed from outside by specifying the namespace)
