##2
##t = 3*16**8 - 4**5 + 3
##S = 0
##while t > 0:
##    a = t % 4
##    if a == 3:
##        S += 1
##    t = t // 4
##print(S)

##3
##t = 2*27**7 + 3**10 - 9
##S = 0
##while t > 0:
##    a = t % 3
##    if a == 0:
##        S += 1
##    t = t // 3
##print(S)

##4
##t = 51*7**12 - 7**3 - 22
##z = []
##while t > 0:
##    a = t % 7
##    z.append(a)
##    t = t // 7
##print(sum(z))

##5
##for x in range(0, 1000):
##    t = 125**200 - 5**x + 74
##    z = []
##    while t > 0:
##        a = t % 5
##        z.append(a)
##        t = t // 5
##    if z.count(4) == 100:
##        print(x)
    
##6
##for x in range(1, 5000):
##    t = 4**2015 + 2**x - 2*2015 + 15
##    k = 0
##    while t > 0:
##        a = t % 2
##        if a == 1:
##            k += 1
##        t = t // 2
##    if k == 500:
##        print(x)

##7
##for x in range(1, 4000):
##    t = 4**1014 - 2**x + 12
##    k = 0
##    while t > 0:
##        a = t % 2
##        if a == 0:
##            k += 1
##        t = t // 2
##    if k == 2000:
##        print(x)

##8
##for x in range(1, 4000):
##    t = 36**17 - 6**x + 71
##    S = 0
##    while t > 0:
##        k = t % 6
##        S += k
##        t = t // 6
##    if S == 61:
##        print(x)

##9
##t = 6*144**26 + 11*12**75 - 48
##k = 0
##while t > 0:
##    a = t % 12
##    if a == 11:
##        k += 1
##    t = t // 12
##print(k)

##10
##t = 5*216**1156 - 4 * 36**1147 + 6**1153 - 875
##nul = 0
##five = 0
##while t > 0:
##    a = t % 6
##    if a == 5:
##        five +=1
##    if a == 0:
##        nul += 1
##    t = t // 6
##
##print(five - nul)

##11
##for x in range(1, 20):
##    try:
##        if int('33', x+4) - int('33', 4) == 33:
##            print(x)
##    except:
##        continue;

##12
##for N in range(0, 20):
##    try:
##        if int('103', N) == int('97', N+2):
##            print(N)
##    except:
##        ...

##13
##for N in range(0, 30):
##    try:
##        if int('132', N) + int('13', 8) == int('124', N+1):
##            print(N)
##    except:
##        continue;

##14
##for x in range(0, 40):
##    try:
##        if int('21', x) * int('13', x) == int('313', x):
##            print(x)
##    except:
##        ...

##15
##for x in range(20, 31):
##    try:
##        if x % int('100', 3) == int('11', 3):
##            print(x)
##    except:
##        ...

##16
##for x in range(0, 41):
##    if x % int('10000', 2) == int('1011',2):
##        print(x)

##17
##for N in range(0, 20):
##    try:
##        if int('1000', N) <= 68 <= int('10000', N) and 68 % int('10', N) == int('2', N):
##            print(N)
##    except:
##        ...

##18
##for N in range(0, 1000):
##    try:
##        if int('10', 6) <= N < int('100', 6) and int('100', 5) <= N < int('1000', 5) and N % int('10', 11) == 1:
##            print(N)
##    except:
##        ...

##19
##for N in range(1, 1000):
##    if int('10', 7) <= N < int('100', 7) and int('100', 6) <= N < int('1000', 6) and N % int('10', 13) == int('3', 13):
##        print(N)

20
k = 0
for N in range(1, 10000):
    if N < int('10000', 5) and N > int('10000', 2) and N % int('10', 16) == int('C', 16):
        k += 1
print(k)







