top_num = int(input('number: '))
total = 0
for n in range(1, top_num + 1):
    total = total + n
    print('DEBUG: n = ', n, 'total = ', total)
print('Sum of numbers 1 to', top_num, 'is', total)
