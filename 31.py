from itertools import count
from optparse import Values


def same_by(characteristic,object):
    count = 0
    for element in object:
        if characteristic(element) == 0:
            count += 1
    return len(object) == count


values = [0, 2, 10, 6]
if same_by(lambda x:x % 2, values):
    print('same')
else:
    print('different')