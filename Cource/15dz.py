##1
##def F(x, a):
##    return (x % a == 0 and x % 24 and x % 16 != 0) <= (x % a != 0) 
##for a in range(1, 1000):
##    if all(F(x, a) for x in range(0, 10000)):
##        print(a)

##2
##def F(x, a):
##    return (x % 84 != 0 or x % 90 != 0) <= (x % a != 0)
##for a in range(1, 5000):
##    if all(F(x, a) for x in range(1, 10001)):
##        print(a)
##
##3
##def F(x, a):
##    return ((x % 15 == 0) and (x % 21 != 0)) <= (x % a != 0 or x % 15 != 0)
##for a in range(1, 5000):
##    if all(F(x, a) for x in range(1, 10001)):
##        print(a)
##
##4
##def F(x, a):
##    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)
##for a in range(1, 10001):
##    if all(F(x, a) for x in range(1, 10001)):
##        print(a)
##5
##def F(x, a):
##    return (a % 7 == 0) and (240 % x == 0) <= ((a % x != 0) <= (780 % x != 0))
##for a in range(1, 1000):
##    if all(F(x, a) for x in range(1, 10001)):
##        print(a)
##6
##def F(x, a):
##    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))
##for a in range(1, 300):
##    if all(F(x, a) == 1 for x in range(1, 10000)):
##        print(a)
##7
##def F(x, a):
##    return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))
##for a in range(1, 1000):
##    if all(F(x, a) for x in range(1, 100000)):
##        print(a)
##8
##def F(x, a):
##    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))
##for a in range(1, 300):
##    if all(F(x, a) for x in range(1, 10001)):
##        print(a)
##        break;
##10
##def F(x, y, a):
##    return (x * y > a) and (x > y) and (x < 8)
##for a in range(1, 100):
##    if all(not(F(x, y, a)) for x in range(1, 100) for y in range(1, 100)):
##        print(a)
##        break;
##11 
##def F(x, y, a):
##    return (x > 39) or (y > 26) or (2*x + 4*y < a)
##for a in range(1, 1000):
##    if all(F(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
##        print(a)
##        break;
##12
##def F(x, y, a):
##    return (2*x + y != 70) or (x < y) or (a < x)
##for a in range(1, 100):
##    if all(F(x, y, a) for x in range(0, 1001) for y in range(0, 1001)):
##        print(a)
##13
##def F(x, y, a):
##    return (x**2 - 10 * x + 16 > 0) or (y ** 2 - 10 * y + 21 > 0) or (x * y < 2 * a)
##for a in range(1, 1000):
##    if all(F(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
##        print(a)
##        break;
##15
##A = set()
##B = {3, 6, 9, 12}
##C = {1, 2, 3, 4, 5, 6}
##
##def F(x):
##    return not(not(x in A) and (x in B)) or not(x in C)
##for x in range(0, 1000):
##    if F(x) == 0:
##        A.add(x)
##print(A)
