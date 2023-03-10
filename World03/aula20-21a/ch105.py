def grades(*n,status=False):
    """
    -> Analise the students grades and transform in data.
    :param n: One or more grades.
    :param status: optional, True or False to show the situation.
    :return: dict that shows the data.
    """
    data = {}
    data['total'] = len(n)
    data['higher'] = max(n)
    data['lower'] = min(n)
    data['average'] = sum(n)/len(n)
    if status == True:
        if data['average'] <=5:
            data['status'] = 'BAD'
        elif data['average'] <= 7:
            data['status'] = 'REGULAR'
        elif data['average'] < 10:
            data['status'] = 'GOOD'
        else:
            data['status'] = 'PERFECT'
    return data
resp = grades(10,10,10,status=True)
help(grades)
