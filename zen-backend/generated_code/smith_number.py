def smith_number(n):
    sum = 0
    for i in range(1, n+1):
        if str(i).count('7') + str(i).count('4') == len(str(i)):
            sum += i
    return sum
print(smith_number(100))