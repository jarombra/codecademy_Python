grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
    average = grades_average(grades)
    variance = 0
    for score in grades:
        variance += (average - score) ** 2
        result = variance / float(len(grades))
    return result
print grades_variance(grades)

def grades_std_deviation(variance):
    result = variance ** 0.5
    return result
    variance += grades_variances(grades)
    print grades_std_deviation(variance)
