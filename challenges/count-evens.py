def count_evens(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    print(count) 
    # depending on the indentation of count, it'll either print 1 to 5, or just print 5


count_evens([1, 3, 6, 8, 9, 5, 2, 10, 13, 20])
