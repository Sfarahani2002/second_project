def hello():
    global name 
    name = 'Hassan'
    print(f'in function name is {name}')
    
name = 'Saleh'
print(f'first, name is {name}')
hello()
print(f"second, name is {name}")