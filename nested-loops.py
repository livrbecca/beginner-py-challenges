# loop inside a loop

# 5 times, run the inner loop 3 times
# x is 0-4, y is 0-2

for x in range(5):
    for y in range(3):
        print(f"{x},{y}")

# loop 1: outer loop - first iteration, x is 0,
# loop 2: inner loop, which is a child of the first for loop
# whats inside for the inner loop will be executed 3 times