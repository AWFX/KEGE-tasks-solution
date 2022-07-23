##1
##def f(x, y, z, w):
##    return (x or not(y)) and not(y==z) and w
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if f(x, y, z, w):
##                    print(x, y, z, w)

##2
##def F(a, b, c):
##    return (a and not(c)) or (not(b) and not(c))
##print('a b c')
##for a in 0, 1:
##    for b in 0, 1:
##        for c in 0, 1:
##            print(a, b, c, F(a, b, c))

##3
##def F(x, y, z):
##    return (not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not(y) and not(z))
##print('x y z')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            if F(x, y, z):
##                print(x, y, z)

##4
##def F(x, y, z, w):
##    return ((not(x) and y) == z) and w
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if F(x, y, z, w):
##                    print(x, y, z, w)

##5
##def F(x, y, z, w):
##    return (x <= (y and not(z))) or w
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x,y,z,w)):
##                    print(x, y, z, w)

##6
##def F(x, y, z ,w):
##    return (x and not(y)) or (x == z) or w
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
####                    print(x, y, z, w)

##7
##def F(x, y, z):
##    return (not(x) and y and z) or (not(x) and not(z))
##print('x y z')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            if F(x, y, z):
##                print(x, y, z)

##8
##def F(x, y, z, w):
##    return not(y) and x and (not(z) or w)
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if F(x, y, z, w):
##                    print(x, y, z, w)
##
##9
##def F(x, y, z, w):
##    return (y <= (x or z)) and (z <= y)
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)

##10
##def F(x, y, z):
##    return not(x == (y <= z))
##print('x y z')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            print(x, y, z, F(x, y, z))

##11
##def F(x, y, z, w):
##    return (y <= x) or not((x <= z) and (z <= x)) and not(w)
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)

##12
##def F(x, y, z, w):
##    return not(w) and ((y or z) <= (not(x) and y))
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if F(x, y, z, w):
##                    print(x, y, z, w)

##13
##def F(x, y, z, w):
##    return ((w <= y) or not(y <= z)) and not(x) and not(x == z)
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if F(x, y, z, w):
##                    print(x, y, z, w)
                    
##14
##def F(x, y, z, w):
##    return (x <= y) or not(w <= z)
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)
                
##15
##def F(a, b, c, d):
##    return ((a and b) == (not(c))) and (b <= d)
##print('a b c d')
##for a in 0, 1:
##    for b in 0, 1:
##        for c in 0, 1:
##            for d in 0, 1:
##                if F(a, b, c, d):
##                    print(a, b, c, d)

##16
##def F(x, y, z, w):
##    return not(z and not(w)) or ((z <= w) == (x <= y))
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)

##17
##def F(a, b, c, d):
##    return (not(a) and not(b)) or (b == c) or d
##print('a b c d')
##for a in 0, 1:
##    for b in 0, 1:
##        for c in 0, 1:
##            for d in 0, 1:
##                if not(F(a, b, c, d)):
##                    print(a, b, c, d)
##

##18
##def F(x, y, z, w):
##    return ((z <= x) and (x <= w)) or (y == (z or x))
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)

##19
##def F(x, y, z, w):
##    return (x and z) or ((w <= x) == (z <= y))
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)

##20
##def F(x, y, z, w):
##    return (x == (not(z))) <= ((x or w) == y)
##print('x y z w')
##for x in 0, 1:
##    for y in 0, 1:
##        for z in 0, 1:
##            for w in 0, 1:
##                if not(F(x, y, z, w)):
##                    print(x, y, z, w)
