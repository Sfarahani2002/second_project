donations = {
    'saleh': 200,
    'ali': 400,
    'arian': 10,
    'hasan': 9
}

def donationa_analysis(don):
    person = ''
    total = 0
    count = 0 
    max_donation = -1
    for name, value in don.items():
        total += value
        count += 1
        if value > max_donation:
            person = name 
            max_donation = value
    average = total / count 
    return average, total, person

avg, total, max_person = donationa_analysis(donations)
print(f'total donations {total}')
print(f'average donations is {avg}')
print(f'thanks to {max_person}')