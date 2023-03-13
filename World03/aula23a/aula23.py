try:
    a = int(input('Number 1: '))
    b = int(input('Number 2: '))
    c = a/b
except (ValueError, TypeError):
    print('Type a valid data.')
except ZeroDivisionError:
    print('Cannot divid a number by zero.')
except KeyboardInterrupt:
    print('User let the input in blank.')
except Exception as error:
    print(error.__cause__)
else:
    print(c)
finally:
    print('Ok')
