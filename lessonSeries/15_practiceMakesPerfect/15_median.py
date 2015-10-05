def median(lists):
    lists = sorted(lists)
    n = len(lists)
    if n % 2 == 0:
        return (lists[n / 2 - 1] + lists[n / 2]) / 2.0
    else:
        return lists[(n/2)]

print median([1, 2, 4])

# Or...

import numpy

def median(list):
    return numpy.median(list)

print median([1, 2, 3, 4, 5])
