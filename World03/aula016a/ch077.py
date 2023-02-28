list = ('Sky','Anime','Manga','Game','Nihongo','Programming','Notebook','Smartphone')

for c in list:
    print('\nIn the word {} we have: '.format(c.upper()), end='')
    for l in c.lower():
        if l.lower() in 'abcde':
            print(l, end=' ')