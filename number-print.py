count = 0 # variable to count the even numbers, each time one is found, increment

for number in range(1, 21):  # range replaces writing an array from 1-10
    if number % 2 == 0:  # finding even number
        count += 1
        print(number)

print(f"we have {count} even numbers")
