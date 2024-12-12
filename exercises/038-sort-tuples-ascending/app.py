from operator import itemgetter

def sort_tuples_ascending(data):
    tuples = [tuple(tup.split(',')) for tup in data]
    sorted_tuples = sorted(tuples, key=itemgetter(0,1,2))
    return sorted_tuples