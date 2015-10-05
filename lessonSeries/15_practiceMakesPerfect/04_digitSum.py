def digit_sum(n):
    num = []
    s = str(n)
    total = 0
    for string in s:
        string = int(string)
        num.append(string)
    for i in num:
        total = total + i
    return total
    
# Or...

def digit_sum(n):
    s = str(n)
    total = 0
    for string in s:
        total += int(string)
    return total
    
# Or...

def digit_sum(n):
    num = 0
    count = len(str(n))
    while count != 0:
        temp = n % 10
        num += temp
        n = n / 10
        temp = 0
        count -= 1
    return num
