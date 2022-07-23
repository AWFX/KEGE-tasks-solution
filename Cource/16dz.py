##1
##def f(n):
##    if n == 0:
##        return 1
##    if n == 1:
##        return 3
##    if n == 2:
##        return 2
##    if n > 2:
##        return f(n-1) * f(n-3)
##print(f(7))

##2
##def f(n):
##    if n <= 3:
##        return n
##    if n > 0 and n % 3 == 0:
##        return n*n*n + f(n-1)
##    if n > 3 and n % 3 == 1:
##        return 4 + f(n // 3)
##    if n > 3 and n % 3 == 2:
##        return n * n + f(n - 2)
##print(f(100))

##3
##def f(n):
##    if n <= 10:
##        return n
##    if 10 < n <= 36:
##        return n // 4 + f(n - 10)
##    if n > 36:
##        return 2 * f(n-5)
##print(f(100))

##4
##def f(n):
##    if n == 1:
##        return 2
##    if n > 1:
##        return f(n-1) + 5 * n**2
##print(f(39))

##5
##def f(n):
##    if n < 5:
##        return 1 + 2 * n
##    if n >= 5 and n % 3 == 0:
##        return 2 * (n + 1) * f(n - 2)
##    if n >= 5 and n % 3 != 0:
##        return 2 * n + 1 + f(n - 1) + 2 * f(n - 2)
##print(f(15))

##6
##def F(n):
##    if n <= 1:
##        return 1
##    if n > 1 and n % 2 == 0:
##        return 3 * n + F(n - 1)
##    if n > 1 and n % 2 != 0:
##        return 2 * F(n - 2) 
##print(F(31))

##7
##def F(n):
##    if n <= 3:
##        return 3
##    if n > 3 and n % 2 == 0:
##        return F(n // 2) + 5
##    if n > 3 and n % 2 != 0:
##        return F(n - 1) - F(n - 2)
##print(F(20))

##8
##def F(n):
##    if n == 1:
##        return 1
##    if n == 2:
##        return 2
##    if n > 2 and n % 2 == 0:
##        return int((n + F(n - 2)) / 5)
##    if n > 2 and n % 2 != 0:
##        return int((2 * n + F(n - 1) + F(n - 2)) / 4)
##print(F(50))

##9
##def F(n):
##    if n <= 1:
##        return 0
##    if n > 1 and n % 2 != 0:
##        return F(n-1) + 3*n**2
##    if n > 1 and n % 2 == 0:
##        return n / 2 + F(n - 1) + 2
##print(F(49))

##10
##def G(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return F(n - 1) + 2 * G(n - 1)
##def F(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return F(n - 1) - n * G(n - 1)
##print(G(18))
##    
    
##11
##from functools import *
##
##@lru_cache(None)
##def F(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return F(n - 1) - 2 * G(n - 1)
##def G(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return F(n - 1) + G(n - 1) + n
##print(sum(int(d) for d in str(G(36))))

##12
##from functools import *
##
##@lru_cache(None)
##def F(n):
##    if n == 0:
##        return 1
##    if n == 1:
##        return 3
##    if n > 1:
##        return F(n-1) - F(n-2) + 3 * n
##print(F(40))

##13
##def F(n):
##    if n <= 18:
##        return n + 3
##    if n > 18 and n % 3 == 0:
##        return (n // 3) * F(n // 3) + n - 12
##    if n > 18 and n % 3 != 0:
##        return F(n - 1) + n**2 + 5
##k = 0
##for i in range(1, 1001):
##    g = F(i)
##    if all(int(d) % 2 == 0 for d in str(g)):
##        k += 1
##print(k)

##14
##def F(n):
##    if n > 30:
##        return n * n + 5 * n + 4
##    if n <= 30 and n % 2 == 0:
##        return F(n+1) + 3 * F(n+4)
##    if n <= 30 and n % 2 != 0:
##        return 2 * F(n+2) + F(n+5)
##k = 0
##for x in range(1, 1001):
##    if sum(int(a) for a in str(F(x))) == 27:
##        k += 1
##print(k)

##15
##def F(n):
##    if n == 0:
##        return 0
##    if n > 0 and n % 2 == 0:
##        return F(n / 2)
##    if n % 2 != 0:
##        return 1 + F(n - 1)
##k = 0
##for x in range(1, 501):
##    if F(x) == 8:
##        k += 1
##print(k)

##16
##def F(n):
##    if n == 1:
##        return 1
##    if n >= 2 and n % 2 == 0:
##        return F(n / 2) + 1
##    if n >= 2 and n % 2 != 0:
##        return F(n - 1) + n
##for x in range(0, 1000):
##    if F(x) == 19:
##        print(x)

##17
##def F(n):
##    k = 1
##    if n >= 1:
##        k += 2 + F(n - 1) + F(n - 3)
##    return k
##print(F(40))

##18
##def F(n):
##    k = n * n
##    if n > 1:
##        k += 2 * n + 1 + F(n-2) + F(n // 3)
##    return k
##print(F(100))

##19
##def F(n):
##    if n <= 1:
##        return n
##    if n > 1 and n % 3 == 0:
##        return n + F(n / 3)
##    if n > 1 and n % 3 != 0:
##        return n + F(n + 3)
##for x in range(1, 1000):
##    try:
##        print(x, F(x))
##    except: RecursionError
##    ...

##20
##def F(n):
##    if n < 3:
##        return n + 1
##    if n >= 3 and n % 2 == 0:
##        return F(n - 2) + n - 2
##    if n >= 3 and n % 2 != 0:
##        return F(n + 2) + n + 2
##k = 0
##for x in range(1, 1000):
##    try:
##        if 10000 <= F(x) < 100000:
##            k +=1
##    except: RecursionError
##print(k)














