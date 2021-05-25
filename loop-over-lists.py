letters = ['a', 'b', 'c']

# enumerate to add index of each item
# returns a tuple in each iteration 
# letter [0] returns the indexes
# [1] would return the item

for letter in enumerate(letters):
    print(letter[0])