print(type(range(5))) # returns range, a complex type

# range object is iterable, means you can iterate over it or use it in a for loop
# means you can write code like the following:
# for x in range(5):

# same for strings, they are also iterable
# x will hold one character in this string
for x in "Python":
    print(x, "*")

# another complex type - list

for x in [1,2,3,4]:
    print(x)