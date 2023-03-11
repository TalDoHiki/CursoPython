def vote(bd):
    from datetime import date
    age = date.today().year - bd
    if age < 16:
        return f'{age} years old. DENIED.'
    elif age < 18 or age >= 65:
        return f'{age} years old. OPTIONAL.'
    else:
        return f'{age} years old. OBRIGATORY.'
brye = int(input('Year of birth: '))
print(vote(brye))
