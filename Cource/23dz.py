##1
##def f(x, y):
##    if x > y: return 0
##    if x == y: return 1
##    if x < y: return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)
##print(f(1, 15))

##2
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x * 2, y) + f(x*x, y)
##print(f(5,154))

##3
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x + 2, y) + f(x * 4, y)
##print(f(1, 13))

##4
##def f(x, y):
##    if x < y:
##        return 0
##    if x == y:
##        return 1
##    if x > y:
##        return f(x - 2, y) + f(x - 5, y)
##print(f(23, 2))

##5
##def f(x, y):
##    if x < y:
##        return 0
##    if x == y:
##        return 1
##    if x > y:
##        return f(x - 1, y) + f(x - 3, y) + f(x // 3, y)
##print(f(22, 2))

##6
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x*2, y)
##print(f(1, 10) * f(10,20))

##7
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x * 2, y)
##print(f(1, 12) * f(12, 30))

##8
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)
##print(f(3, 9) * f(9, 12) * f(12, 20))
##

##9
##def f(x, y):
##    if x < y:
##        return 0
##    if x == y:
##        return 1
##    if x > y:
##        return f(x - 8, y) + f(x // 2, y)
##print(f(102, 43) * f(43, 5))

##10
##def f(x, y):
##    if x > y or x == 6:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 2, y) + f(x * 3, y)
##print(f(1, 25) * f(25, 63))

##11
##def f(x, y):
##    if x > y or x == 11 or x == 18:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
##print(f(4, 8) * f(8, 23))

##12
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y and x % 2 == 0:
##        return f(x + 1, y) + f(x * 2, y) + f(x * 2 + 1, y) + f(x * 10, y)
##    return f(x + 1, y) + f(x * 2 + 1, y) + f(x * 2, y) + f(x * 10, y)
##print(f(1, 15))
        
##13
##def f(x, y):
##    if x > y or x == 43:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 2, y) + f(x + (x - 1), y) + f(x + (x + 1), y)
##print(f(7, 63))

##14
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 1, y) + f(x * 2, y) + f(x * 2 + 1, y)
##print(f(int('100', 2), int('11101', 2)))
##

##15
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x % 10 == 9:
##        return f(x + 1, y) + f(x + 10, y)
##    return f(x + 1, y) + f(x + 11, y)
##print(f(25, 51))

##16
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x % 2 == 0:
##        return f(x + 1, y) + f(x * 1.5, y)
##    return f(x + 1, y)
##print(f(1, 20))

##17
##def f(x, y):
##    if x > y:
##        return 0
##    if x == y:
##        return 1
##    if x < y:
##        return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)
##for x in range(1, 1000):
##    if f(31, x) == 1001:
##        print(x)

##18
##def f(x, y, s):
##    if x > y:
##        return 0
##    if x == y and s == 7:
##        return 1
##    if x == y and s != 7:
##        return 0
##    if x < y:
##        return f(x + 1, y, s + 1) + f(x + 4, y, s + 1) + f(x * 2, y, s + 1)
##print(f(3, 27, 0))

##19
##n = set()
##def f(x, s):
##    if s == 15:
##        n.add(x)
##    else:
##        f(x * 2, s + 1)
##        f(x * 2 + 1, s + 1)
##f(1, 0)
##print(len(n))
    
##20
##n = set()
##def f(x, s):
##        if s == 8:
##            if 1000 <= x <= 1024:
##                 n.add(x)
##        else:
##            f(x + 1, s + 1)
##            f(x + 5, s + 1)
##            f(x * 3, s + 1)
##f(1, 0)
##print(len(n))













