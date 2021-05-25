# breaking out of a loop

successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful!!")
        break # jump out of loop here, without this break, it printed the message 3 times
else:
    print("Attempted 3 times & failed, please try again") # loop never broke