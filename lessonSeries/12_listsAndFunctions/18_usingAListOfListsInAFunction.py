n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        results += numbers
    return results

print flatten(n)

# Or this method works too:

def flatten(lists):
    results = []  
    for lst in lists:
        for num in range(len(lst)):
            results.append(lst[num])
    return results

print flatten(n)

# Or this method works too:

def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results

print flatten(n)
