# Python has a few "basic" data types to get used to
# All variables are very literally "whatever fits" boxes, so a variable is not necessarily stuck being a certain data type
# That adds both versatility AND uncertainty, and, to be fair, there are some functions to check the type of something because of that uncertainty issue
# Sometimes you just need to know what type something is so you don't end up in an unexpected or unplanned for state

# NOTE: a literal is a constant value of some sort, so either an explicitly written string like "your mom", a number like 420, or, I guess, a bytes([66, 65, 66, 65, 66, 65]) (although I'm not sure about the last)
# literals are usually only found on the right side of an assignment operator
# if it's on the left and it works, ask God

# THAT BEING SAID
# Here are the basic data types in python

# NONE : this is a variable with no type. It's useful for error states
my_nothing = None
# Technically it's more correct to say its type is nonetype, which is its own thing
# but remember remember, this is special so instead of == in ifs you use the "is" keyword
# if egg is None

# BOOLEAN : this is a binary unit, a bit, a true or false
my_bool = False

# INTEGER : this is an integer, nothing to explain here
my_int = 420

# FLOAT : this is a floating point number, aka, it has decimals
my_float = 420.69

# COMPLEX : you're not doing 2d math with complex numbers, I KNOW YOU DON'T, but here it is for no reason whatsoever
my_complex_number = 1+3j

# STRING : this is a string, which is an array of characters, although in python, it's more like an object... for... reasons
my_string = "Why does my string of characters have methods?"

##############################################################################
# While string is a basic type, it's also a collection, as in, a list of stuff (you can iterate through each character, etc, etc)
# Specifically, python differentiates between sequence data types (stuff is organized in a certain order) and non-sequential stuff

# Sequence data types:

# STRING (we already did an example)

# LIST : a list of stuff, denoted using brackets like so [a, b, c, d, e, f, g]
my_list = ["Fat Joe", "Billy", "Lenny", "Arthur"]
# A list is a list of variables, so each position can be anything, LITERALLY ANYTHING (remember, vars are boxes of whatever)

# TUPLE : I don't really use this, but it's kinda like a list (no, seriously, who uses this, and why)
my_tuple = ("I", "don't", "get", "why", "this", "exists")

# RANGE : is technically a list of numbers that's automagically generated between two numbers, and with a step, so range(0, 11, 2) would be [0, 2, 4, 6, 8, 10]
# range is immutable, or in normal human speech, it can't be changed. It's a constant once created, so you can imagine the function call above as sytanx sugar more than anything else
# range has 3 arguments: range(start=0, stop, step=1) the only mandatory argument is the stop, so range(3) = [0, 1, 2]
# note that stop is actually never reached. It stops before it uses the stop value, so like a lesser operator instead of a lesser or equal
my_range = range(1990, 2025, 1)

#######################################################################
# Binary data types... which is nice to know, but seriously, at this point, use C or C++

# BYTES : bytes is a sequence of bytes, so a list of 8-bit values]
# a singular byte also exists, technically, but you can't use it by itself
# you can either use the prebuilt "bytes()" function to make a byte list or
# prefix a normal list with "b"
my_bytes_1 = bytes([65, 83, 83])
my_bytes_2 = b"titties"

# bytes is, like range, immutable, so cool for com commands and other stuff, but if you need to change stuff...
# you'd use our next type, BYTEARRAY
# which is explicitly the exact same thing but mutable (can be changed)
my_bytearray = bytearray([66, 79, 79, 66, 83])

# Disclaimer, I've never used this in my life, and it's the first time I hear of it, but it sounds cool for debugging
# MEMORYVIEW : this is a builtin object that allows you to look at the memory of an object, generally stuff that supports the buffer protocol
# examples: bytearray, bytes, arrays using the buffer interface (you have google, use it, when the time comes)
my_memview = memoryview(my_bytearray)

#####################################################################
# DICTIONARY : basically JSON, but in python
my_dictionary = {
    "name": "Patricia",
    "age": 6037,
    420: "Ya, man"
}

# rules: there aren't any. If you use the syntax, everything else goes. Wanna use a nontypical data type for a key? Go for it.
# The way this works is the key you use is hashed and the hash is what's kept and checked against using a hash table
# hence why you can use an object or your dead pet as a key, so long as they're hashable (aka immutable),
# second verse, same as the first, value is a variable, GO WILD, nothing is true, everything is permitted (value can be mutable)
# just don't come to me when everything burns

######################################################################
# Sets, also called unordered collections, is when you put stuff in a bag and when you're reaching in to get it, it comes out in a different order
# there are two types of sets in python

# SET : the one that's used
# defined with a curly bracket instead of straight brackets or parentheses like lists or tuples
# they work in a similar way but the stuff inside is not indexed, instead, you get an iterator and are told "good luck"
# oh, also, all the stuff inside has to be a literal (aka, immutable/constant value, can't be variables)

my_set = {[0, "why", 4.20, False], my_bytes_1, "oh no", my_range}

# see? this is what happens when you stray too far from god
# HERESY

# FROZENSET or frozen set, as the name suggests, is an immutable set BUT NOBODY USUALLY USES THIS
# because the only usage for it is to use it as a key or a subset (since a set can only contain hashable stuff)

my_frozenset = frozenset({"nani", [0, 1, 2], "the fuck"})

# Now, you can basically forget about sets and frozensets, nobody fucking uses them anyway, unless you do data science
# you can also forget bytes, bytearray and memoryview for the time being
# this is a beginner's guide, you only need a towel and a raised thumb
# the answer to all the questions you might have is 42
