##1
##for x in range(0, 2000000):
##    t = x
##    a = 0 
##    b = 0 
##    while t > 0: 
##        a = a + 1 
##        if t % 11 > b:
##            b = t % 11
##        t = t // 11
##    if a == 7 and b == 7:
##        print(x, a, b)
##        break;

##2
##for i in range(0, 200000000):
##    x = i
##    a = 2
##    b = 3
##    while x > 0:
##        d = x % 4
##        a *= d
##        if d < 3:
##            b += d
##        x //= 4
##    if a == 24 and b == 16:
##        print(i)

##4
##for i in range(0, 10000000):
##    for j in range(0, 10000000):
##        x = i
##        y = j
##        a = 0
##        b = 0
##        while x * y > 0:
##            if x > 0:
##                a = a + 1
##            if y > 0 and y % 7 > b:
##                b = y % 7
##            x = x // 10
##            y = y // 7
##        if a == 4 and b == 5:
##            print(i, j)

##6
##for i in range(63, 1000, 3):
##    N = i
##    c = 0; T = 3; d = 3;
##    while N != 0:
##        N = N - T
##        T = T + d
##        c = c + 1
##        if N < 0:
##            i += 3
##    if c % 2 == 0:
##        c = c + d
##    print(c)

##8
##for i in range(100, 1000):
##    x = i
##    L = x - 18
##    M = x + 36
##    while L != M:
##        if L > M:
##            L = L - M
##        else:
##            M = M - L
##    if M == 9:
##        print(i)
##        input()

##9
##for i in range(101, 1000000000):
##    x = i
##    a = 5 * x + 345
##    b = 5 * x - 807
##    if b > 0:
##        while a != b:
##            if a > b:
##                a -= b
##            else:
##                b -= a
##        if a == 96:
##            print(i)
##            input()

##10
##x = 360763
##S = 0
##for y in range(1, 360764):
##    a = x; b = y
##    while b > 0:
##        r = a % b
##        a = b
##        b = r
##    if a == 13:
##        S += 1
##print(S)
