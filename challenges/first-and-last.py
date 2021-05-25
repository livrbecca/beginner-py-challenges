# given an array of ints, print True if first element or last element is 6

def first_last(arr):
    if arr[0] == 6 or arr[-1] == 6:
        print("True")
    else:
        print("False")


first_last([6, 1, 2, 4, 5, 7])
