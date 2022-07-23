##1
##def F(s, c, m):
##    if s >= 34: return c % 2 == m % 2
##    if c == m:
##        return 0
##    h = [F(s+1, c+1, m), F(s+2, c+1, m), F(s+3, c+1, m), F(s * 2, c+1, m)]
##    return any(h) if (c+1)%2 == m % 2 else all(h)
##
##for s in range(1,33):
##    for m in range(1,5):
##        if F(s, 0, m) == 1:
##            if m == 2 or m == 4: print(s,m)
##            break

##2
##def F(s, c, m):
##    if 36 <= s <= 60: return c % 2 == m % 2
##    if s > 60: return c % 2 != m % 2
##    if c == m: return 0
##    h = [F(s + 1, c + 1, m), F(s * 2, c + 1, m), F(s * 3, c + 1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for s in range(1, 36):
##    for m in range(1, 5):
##        if F(s, 0, m) == 1:
##            print(s, m)
##            break
    
##3
##def F(a,b,c,m):
##    if a + b >= 59: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a + 1, b, c+1, m),F(a * 2, b, c+1, m), F(a, b + 1, c+1, m), F(a, b * 2, c+1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for b in range(1, 59):
##    for m in range(1, 5):
##        if F(5, b, 0, m) == 1:
##            print(b, m)
##            break

##4
##def F(a,b,c,m):
##    if a + b >= 77: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a+1, b, c+1, m), F(a*2, b, c+1, m), F(a, b+1, c+1, m), F(a, b*2, c+1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for b in range(1, 70):
##    for m in range(1,5):
##        if F(7, b, 0, m) == 1:
##            print(b, m)
##            break

##5
##def F(a, b, c, m):
##    if a + b >= 68: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a+1, b, c+1, m), F(a + b, b, c+1, m), F(a, b+1, c+1, m), F(a, b+a, c+1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for b in range(1, 60):
##    for m in range(1, 6):
##        if F(8, b, 0, m) == 1:
##            if m == 4:print(b, m)
##            break

##6
##def F(a, b, c, m):
##    if a * b >= 63: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a + 1, b, c + 1, m), F(a * 2, b, c + 1, m), F(a, b + 1, c + 1, m), F(a, b * 2, c + 1, m)]
##    return any(h) if (c+1)%2 == m % 2 else all(h)
##
##for b in range(1, 31):
##    for m in range(1, 5):
##        if F(2, b, 0, m) == 1:
##            print(b, m)
##            break

##7
##def F(a, b, g, c, m):
##    if a + b + g >= 73: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a + 3, b, g, c + 1, m), F(a + 13, b, g, c + 1, m), F(a + 23, b, g, c + 1, m), 
##         F(a, b + 3, g, c + 1, m), F(a, b + 13, g, c + 1, m), F(a, b + 23, g, c + 1, m), 
##         F(a, b, g+3, c + 1, m), F(a, b, g + 13, c + 1, m), F(a, b, g + 23, c + 1, m)]
##    return any(h) if (c+1)% 2 == m % 2 else all(h)
##
##for S in range(1, 23):
##    for m in range(1, 5):
##        if F(2, S, 2 * S, 0, m) == 1:
##            print(S, m)
##            break

##8
##def F(a, b, c, m):
##    if a+b <= 20: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(a - 1, b, c + 1, m), F((a+1)//2, b, c + 1, m), F(a, b - 1, c + 1, m), F(a, (b+1)//2, c + 1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for b in range(100, 10, -1):
##    for m in range(1, 5):
##        if F(10, b, 0, m) == 1:
##            if m == 4: print(b,m)
##            break

##9
##def F(s, c, m):
##    if s >= 2163: return c % 2 == m % 2
##    if c == m: return 0
##    h = [F(s + 1, c + 1, m), F(s * 3, c + 1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for s in range(1, 2163):
##    for m in range(1, 5):
##        if F(s, 0, m) == 1:
##            if m == 4: print(s, m)
##            break
        

























