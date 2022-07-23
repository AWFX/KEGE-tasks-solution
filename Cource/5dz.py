##1
##for x in range(1, 1000):
##    t = str(bin(x)[2:])
##    s1 = sum(int(f) for f in t) % 2
##    t += str(s1) 
##    s2 = sum(int(f) for f in t) % 2 
##    t += str(s2)
##    if int(t, 2) > 80:
##        print(int(t, 2))
##        break

##2
##for N in range(1, 1000):
##    R = str(bin(N))[2:]
##    if N % 2 == 0:
##        R += '01'
##    else:
##        R += '10'
##    if int(R, 2) > 81:
##        print(int(R, 2))
##        break
        
##3
##for N in range(1, 1000):
##    R = str(bin(N))[2:]
##    R += R[-1]
##    if R.count('1') % 2 == 0:
##        R += '0'
##    else:
##        R += '1'
##
##    if R.count('1') % 2 == 0:
##        R += '0'
##    else:
##        R += '1'
##    if int(R, 2) > 130:
##        print(N)
##        break

##4
##for N in range(1, 1000):
##    R = str(bin(N))[2:]
##    R += R[-1]
##    if R.count('1') % 2 == 0:
##        R += '0'
##    else: R += '1'
##
##    if R.count('1') % 2 == 0:
##        R += '0'
##    else: R += '1'
##    if int(R, 2) > 144:
##        print(int(R, 2))
##        break
   
##5
##for N in range(11, 1000):
##    R = N
##    t = ''
##    while R > 0:
##        t += str(R % 3)
##        R = R // 3
##    t = t[::-1]
##    t += str(N % 3)
##    if 100 <= int(t, 3) < 1000:
##        print(int(t, 3))
##        break
    
##6
##maxi = 0
##for N in range(1, 100):
##    R = str(bin(N))[2:]
##    R = R[::-1]
##    while R[0] == '0':
##        R = R[1:]
##    if int(R, 2) == 13 and N > maxi:
##        maxi = N
##print(maxi)
        
##7
##a = set()
##for N in range(1, 1000):
##    R = str(bin(N))[2:]
##    S = sum(int(h) for h in R)
##    R += str((S % 2))
##    S = sum(int(h) for h in R)
##    R += str((S % 2))
##    R = int(R, 2)
##    if R < 80:
##        a.add(R)
##print(a, len(a))

##8
##mini = 10000
##for N in range(1, 1000):
##    R = str(bin(N))[2:]
##    if N % 2 == 0:
##        R = '1' + R + '0'
##    else:
##        R = '11' + R + '11'
##    if int(R, 2) > 52 and int(R, 2) < mini:
##        mini = int(R, 2)
##print(mini)

##9
##for N in range(1000, 10000):
##    N = str(N)
##    a = int(N[0]) * int(N[1])
##    b = int(N[2]) * int(N[3])
##    R = ''
##    if a < b:
##        R = str(a) + str(b)
##    else:
##        R = str(b) + str(a)
##    if R == '1214':
##        print(N)
        
##10    
##for N in range(100, 1000):
##    N = str(N)
##    a = int(N[0]) * int(N[1])
##    b = int(N[1]) * int(N[2])
##    R = ''
##    if a > b:
##        R = str(a) + str(b)
##    else:
##        R = str(b) + str(a)
##    if R == '240':
##        print(N)
    
    



















