multiplay = lambda x, y: x * y
print(multiplay(3, 5))


names = ['saleh', 'ali ', ' arshia', 'matin ']
short_names = filter(lambda s: len(s) <= 4, names )

for name in short_names:
    print(name)
    
a = [ 5, 6, 7.7, 8.1, 9, 2, 5]

print(list(filter(lambda x: x != int(x), a)))


b = [3, 5, 6, 7, 1]
tavan_b = map(lambda x: x**2, b)
print(list(tavan_b))