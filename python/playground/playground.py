def prime(n):
    flag = False

    for i in range(2, n):
        if n % 2 == 0:
            flag = True
            break
    if flag:
        print("not prime")
    else:
        print("prime")


prime(28)
