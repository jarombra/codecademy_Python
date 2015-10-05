def purify(lis):
    lis2 = []
    for num in lis:
        if num % 2 == 0:
            lis2.append(num)
    return lis2
