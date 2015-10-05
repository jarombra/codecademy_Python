grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for x in scores:
        total += x
    return total
    
def grades_average(grades):
    total = grades_sum(grades)
    avg = total/float(len(grades))
    return avg
        
print grades_average(grades)
