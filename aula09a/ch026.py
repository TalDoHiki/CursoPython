phrase = str(input('Type something: '))

print('The character "A" show in a total of {} times, being the first time {} and the last time {}'.format(phrase.lower().count('a'), phrase.find('a'), phrase.rfind('a')))