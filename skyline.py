def skyline(*args):
    tallest = args[0]
    for num in args:
        if num > tallest:
            tallest = num
    return tallest 
    return 0
         
print(skyline(200, 700, 4991))


def pick_evens(*args):
    evens = []
    for num in args:
        if num %2 == 0:
        
            evens.append(num)
    return evens

print(pick_evens(1, 4, 20, 3, 5, 7, 19,40))