# and - if BOTH conditions true
# or - if AT LEAST ONE of the conditions are true
# not

# using == here is redudant, would be comparing true with true, just write the variable name
high_income = False
good_credit = True
student = False


# if high_income or good_credit:
#     print("Allowed loan")
# else:
#     print("not allowed loan")


# if not student:
#     print("Allowed loan")
# else:
#     print("not allowed loan")



if (high_income or good_credit) and not student: # only one condition in brackets needs to be true
    print("Allowed loan")
else:
    print("not allowed loan")
