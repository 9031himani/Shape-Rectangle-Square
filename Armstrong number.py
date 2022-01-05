for num in range(1,1001):

    digits = len(str(num))

    sum = 0
    p = num

    while (p!=0):
        q = p%10
        sum += pow(q, digits)
        p = p // 10



    if num == sum:
        print(f"{num} ")









