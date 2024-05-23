def bank(x, y):
    for i in range (1, y+1):
        count = x + (x * 0.1)
        x = count
    print (round(count, 1))
x = int(input("Введите первоначальную сумму вклада: "))
y = int(input("Введите желаемый срок вклада: "))
bank(x, y)




