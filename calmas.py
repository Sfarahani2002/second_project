def calculate_masaht(**kwargs):
    print(f"kwargs is {kwargs}")
    if 'tool' in kwargs:
        return kwargs['tool'] * kwargs[ 'ertefa']
    if 'shoa' in kwargs:
        return kwargs['shoa'] * 3.1415926 * kwargs['shoa']
    return 100 

print(calculate_masaht(shoa=5))