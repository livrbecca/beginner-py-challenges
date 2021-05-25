# for loop iterating 3 times, in each iteration number will have a different value
# add +1 if you dont want the index to start from 0

#  (number + 1) * "." only refers to the dot's

for number in range(3):
    print("Hello, this is your invite", number + 1, (number + 1) * ".")


# if you change range, you dont need to add + 1
# range: 1-4, but will not include 4

for number in range(1, 4):
    print("Hello, you've been uninvited", number, (number) * ".")