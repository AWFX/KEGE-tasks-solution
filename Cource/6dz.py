##1
##for s in range(0, 1000):
##    n = 1024
##    t = s
##    while s >= 5:
##        s -= 5
##        n = n // 2
##    if n == 64:
##        print(t)

##2
##for s in range(0, 1000):
##    n = 1
##    t = s
##    while s <= 80:
##        s += 7
##        n *= 3
##    if n == 81:
##        print(t)

##3
##for s in range(0, 1000):
##    n = 1
##    t = s
##    while s < 94:
##        s += 8
##        n *= 2
##    if n == 128:
##        print(t)

##4
##for s in range(0, 1000):
##    n = 1
##    t = s
##    while s <= 45:
##        s += 4
##        n *= 2
##    if n == 256:
##        print(t)

##5
##k = 0
##for i in range(1, 1000):
##    d = i
##    n = 27
##    s = 12
##    while s <= 2019:
##        s = s + d
##        n = n + 16
##    if n == 171:
##        k += 1
##print(k)

##6
##for i in range(1, 1000):
##    d = i
##    n = 1
##    while d // n > 0:
##        d = d - 2
##        n = n + 3
##    if n == 46:
##        print(i)

##7
##for i in range(1, 1000):
##    s = i
##    n = 3
##    while s < 220:
##        s = s + 6
##        n = n + 3
##    if n > 40:
##        print(i)

##8
##k = 0
##for i in range(1, 1000):
##    s = i
##    n = 3
##    while s * n < 243:
##        s = s // 3
##        n = n * 9
##        if n > 1000: break
##    if n == 27:
##        print(i)
##        k += 1
##print(k)

##9
##k = 0
##for i in range(1, 1000):
##    d = i
##    n = 20
##    s = 40
##    flag = True
##    while s + n < d:
##        s = s - 10
##        n = n - 10
##        if n < -1000:
##            flag = False
##            break
##            
##    if flag:
##        print (n, i)
##        k += 1
##print(k)

##10
##for i in range(0, 1000):
##    s = i
##    n = 100
##    while s - n >= 100:
##        s = s + 20
##        n = n + 40
##    if i != s:
##        print(i)
##        input()


