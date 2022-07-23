##1
##def F(x):
##    d = set()
##    for i in range(2, int(x ** 0.5) + 1):
##        if x % i == 0:
##            d.add(i)
##            d.add(x // i)
##    return sorted(d)
##
##for i in range(174457, 174506):
##    d = F(i)
##    if len(d) == 2:
##        print(*d)

##2
##def F(x):
##    d = set()
##    for i in range(2, int(x**0.5) + 1):
##        if x % i == 0:
##            d.add(i)
##            d.add(x // i)
##    return sorted(d)
##
##for i in range(81234, 134690):
##    d = F(i)
##    if len(d) == 3:
##        print(*d)

##3
##def F(x):
##    d = set()
##    for i in range(1, int(x**0.5) + 1):
##        if x % i == 0:
##            d.add(i)
##            d.add(x // i)
##    return sorted(d)
##
##for i in range(154026, 154044):
##    d = F(i)
##    if len(d) == 4:
##        print(d[2], d[3])

##4
##def F(x):
##    d = set()
##    for i in range(2, int(x ** 0.5) + 1):
##        if x % i == 0:
##            d.add(i)
##            d.add(x // i)
##    return sorted(d)
##
##for i in range(150000, 150150):
##    d = F(i)
##    f = sum(g for g in d)
##    if f % 13 == 10:
##        print(i, f)

##5
##def F(x):
##    d = set()
##    for i in range(2, int(x**0.5) + 1):
##        if x % i == 0:
##            d.add(i)
##            d.add(x//i)
##    return sorted(d)
##
##for i in range(250201, 251300):
##    d = F(i)
##    if len(d) >= 2:
##        M = max(d) + min(d)
##        if M % 123 == 17:
##            print(i, M)
##    

6
def F(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for i in range(550001, 550100):
    d = F(i)
    if len(d) > 0:
        g = sum(d) // len(d)
        if g % 31 == 13:
            print(i, g)
































