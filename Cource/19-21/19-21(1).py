##1
##def F(s, c, m):
##    if s >= 21: return c % 2 == m % 2
##    if c == m:
##        return 0
##    h = [F(s+1, c+1, m), F(s+2, c+1, m), F(s+3, c + 1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for s in range(1,21):
##    for m in range(1, 8):
##        if F(s, 0, m) == 1:
##            print(s, m)
##            break

##2
##def F(s,c,m):
##    if s == 0: return c%2 == m % 2
##    if c == m: return 0
##    h = [F(s - 1, c + 1, m), F(s - 2, c + 1, m), F(s - 4, c + 1, m)]
##    return any(h) if (c+1)%2 == m % 2 else any(h)
##
##for s in range(15, 1, -1):
##    for m in range(1, 10):
##        if F(s,0,m) == 1:
##            print(s, m)
##            break

##3
##def F(s, c, m):
##    if s >= 65: return c%2 == m%2
##    if c == m: return 0
##    h = [F(s+1,c+1,m), F(s+2,c+1,m), F(s*3,c+1,m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for s in range(1, 65):
##    for m in range(1, 7):
##        if F(s,0,m) == 1:
##            if m == 4: print(s,m)
##            break

##4
##def F(s, c, m):
##    if 43 <= s <= 72: return c % 2 == m % 2
##    if s > 72: return c % 2 != m % 2
##    if c == m: return 0
##    h = [F(s + 1, c + 1, m), F(s * 2, c + 1, m), F(s * 3, c + 1, m)]
##    return any(h) if (c+1) % 2 == m % 2 else all(h)
##
##for s in range(1, 43):
##    for m in range(1, 5):
##        if F(s, 0, m) == 1:
##            print(s, m)
##            break

































