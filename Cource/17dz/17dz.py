##1
##with open('1.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##maxi = 0
##for i in range(0, len(s)):
##    if s[i] % 3 == 0 and s[i] % 7 != 0 and s[i] % 17 != 0 and s[i] % 19 != 0 and s[i] % 27 != 0:
##        k += 1
##        if s[i] > maxi:
##            maxi = s[i]
##print(k, maxi)

##2
##with open('2.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mini = 10000
##for i in range(0, len(s)):
##    if (s[i] % 10 == 2 or s[i] % 10 == 7) and s[i] % 3 == 0 and s[i] % 11 == 0:
##        k += 1
##        if s[i] < mini:
##            mini = s[i]
##print(k, mini)

##3
##with open('3.txt') as f:
##    s = [int(x) for x in f]
##
##mini = 10000
##maxi = 0
##k = 0
##for i in range(0, len(s)):
##    if (s[i] % 10 == 5 or s[i] % 10 == 7) and s[i] % 9 != 0 and s[i] % 11 != 0:
##        k += 1
##        if s[i] > maxi:
##            maxi = s[i]
##        elif s[i] < mini:
##            mini = s[i]
##print(k, maxi + mini)

##4
##with open('4.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##maxi = 0
##mini = 10000
##for i in range(0, len(s)):
##    if s[i] % 13 == 7 and s[i] % 7 != 0 and s[i] % 11 != 0:
##        k += 1
##        if s[i] > maxi:
##            maxi = s[i]
##        elif s[i] < mini:
##            mini = s[i]
##print(maxi - mini, k)

##5
##with open('5.txt') as f:
##    s = [int(x) for x in f]
##
##S = 0
##k = 0
##for i in range(0, len(s)):
##    if s[i] % 16 == 11 and s[i] % 7 == 0 and s[i] % 6 != 0 and s[i] % 13 != 0 and s[i] % 19 != 0:
##        k += 1
##        S += s[i]
##print(S, k)

##6
##with open('6.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mS = -10000
##for i in range(0, len(s) - 1):
##    if (s[i] + s[i + 1]) % 3 == 0 and (s[i] + s[i + 1]) % 6 != 0 and abs(s[i] * s[i + 1]) % 10 == 8:
##        k += 1
##        if (s[i] + s[i + 1]) > mS:
##            mS = s[i] + s[i + 1]
##print(k, mS)

##7
##with open('7.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mini = 10000000
##for i in range(0, len(s) - 1):
##    if (s[i] * s[i + 1]) > 0 and (s[i] + s[i + 1]) % 7 == 0:
##        k += 1
##        if (s[i] * s[i + 1]) < mini:
##            mini = s[i] * s[i + 1]
##print(k, mini)

##8
##with open('8.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mS = -10000000
##for i in range(1, len(s) - 1):
##    if (s[i - 1] * s[i] * s[i + 1]) % 7 == 0 and (s[i - 1] + s[i] + s[i + 1]) % 10 == 5:
##        k += 1
##        if s[i - 1] + s[i] + s[i + 1] > mS:
##            mS = s[i - 1] + s[i] + s[i + 1]
##print(k, mS)

##9
##with open('9.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mini = 10000000
##for i in range(1, len(s) - 1):
##    if (s[i - 1] % 12 == 0 or s[i] % 12 == 0 or s[i+1] % 12 == 0) and s[i - 1] % 3 == 0 and s[i] % 3 == 0 and s[i + 1] % 3 == 0 :
##        k += 1
##        if (s[i-1] + s[i] + s[i+1]) / 3 < mini:
##            mini = (s[i-1] + s[i] + s[i+1]) / 3
##print(k, mini)

##10
##with open('10.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##S = 0
##for i in range(1, len(s) - 1):
##    if s[i - 1] % 3 == 2 or s[i] % 3 == 2 or s[i + 1] % 3 == 2:
##        k += 1
##        S += min(s[i - 1], s[i], s[i + 1])
##print(k, S)
            
##11
##with open('11.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mini = 100000000
##for i in range(1, len(s) - 2):
##    if s[i - 1] > s[i] > s[i + 1] > s[i + 2] and s[i - 1] - s[i + 2] > 1000:
##        k += 1
##        if s[i - 1] + s[i] + s[i + 1] + s[i + 2] < mini:
##            mini = s[i - 1] + s[i] + s[i + 1] + s[i + 2]
##print(k, mini)

##12
##with open('12.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##maxi = -10000000
##for i in range(0, len(s)-1):
##    if s[i] + s[i + 1] >= 100 and (s[i] < 0 or s[i + 1] < 0):
##        k += 1
##        if s[i] * s[i + 1] > maxi:
##            maxi = s[i] * s[i + 1]
##print(k, maxi)

##13
##with open('13.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##mini = 10000000
##for i in range(0, len(s) - 1):
##    if 50 <= abs(s[i - 1]) + abs(s[i]) <= 200:
##        k += 1
##        if min(s[i - 1], s[i]) < mini:
##            mini = min(s[i - 1], s[i])
##print(k, mini)

##14
##with open('14.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##maxi = -110000101
##for i in range(1, len(s) - 1):
##    sr = sum(g for g in s) / len(s)
##    flag = 0
##    if s[i - 1] > sr:
##        flag += 1
##    if s[i] > sr:
##        flag += 1
##    if s[i + 1] > sr:
##        flag += 1
##    if flag >= 2:
##        k += 1
##        if s[i - 1] + s[i] + s[i + 1] > maxi:
##            maxi = s[i - 1] + s[i] + s[i + 1]
##print(k, maxi)

##15
##with open('15.txt') as f:
##    s = [int(x) for x in f]
##
##m = -1000000
##mi = 100000000000
##k = 0
##for i in range(len(s)):
##    if s[i] % 19 == 0 and s[i] > m:
##        m = s[i]
##
##for i in range(0, len(s) - 1):
##    if s[i - 1] > m or s[i] > m:
##        k += 1
##        if s[i - 1] + s[i] < mi:
##            mi = s[i - 1] + s[i]
##print(k, mi)
##        

##16
##with open('16.txt') as f:
##    s = [int(x) for x in f]
##
##k11 = 0
##mini11 = 100000000
##k17 = 0
##maxi17 = 100000000
##for i in range(0, len(s)):
##    if s[i] % 11 == 0:
##        k11 += 1
##        if s[i] < mini11:
##            mini11 = s[i]
##    if s[i] % 17 == 0:
##        k17 += 1
##        if s[i] > maxi17:
##            maxi17 = s[i]
##if k11 > k17:
##    print(k11, mini11)
##else:
##    print(k17, mini17)

##17
##with open('17.txt') as f:
##    s = [int(x) for x in f]
##k = []
##for i in range(len(s)):
##    if s[i] % 4 == 0:
##        k.append(s[i])
##S = min(k) + max(k)
##print(S)
##
##maxi = -1100101
##K = 0
##for i in range(len(s) - 1):
##    if s[i] + s[i+1] < S:
##        K += 1
##        if s[i] + s[i+1] > maxi:
##            maxi = s[i] + s[i+1]
##print(K, maxi)
    
##18
##with open('18.txt') as f:
##    s = [int(x) for x in f]
##
##k = 0
##maxi = -100101010
##for i in range(len(s) - 1):
##    if (s[i] % 9 == 0 and s[i + 1] % 9 != 0 and s[i + 1] % 8 == 3) or (s[i + 1] % 9 == 0 and s[i] % 9 !=0 and s[i] % 8 == 3):
##        k += 1
##        maxi = max(maxi, s[i], s[i + 1])
##print(k, maxi)

##19
##with open('19.txt') as f:
##    s = [int(x) for x in f]
##
##maxi = -10000000
##k = 0
##for i in range(len(s) - 2):
##    flag = 0
##    if not(s[i] > 0 and s[i] % 10 == 9) and (s[i + 1] > 0 and s[i + 1] % 10 == 9) and not(s[i + 2] > 0 and s[i + 2] % 10 == 9):
##        k += 1
##        if s[i] + s[i + 1] + s[i + 2] > maxi:
##            maxi = s[i] + s[i + 1] + s[i + 2]
##print(k, maxi)
        
##20
##with open('20.txt') as f:
##    s = [int(x) for x in f]
##
##Su = 0
##for i in range(len(s)):
##    if s[i] % 35 == 0:
##        Su += sum(int(g) for g in str(s[i]))
##
##k = 0
##mini = 10010101010
##for i in range(0, len(s) - 1):
##    if (s[i] > Su and s[i + 1] <= Su and s[i + 1] % 16 == 15 and s[i + 1]//16 % 16 == 14) or \
##       (s[i + 1] > Su and s[i] % 16 == 15 and s[i]//16 % 16 == 14 and s[i] <= Su):
##        k += 1
##        if s[i] + s[i + 1] < mini:
##            mini = s[i] + s[i + 1]
##print(k, mini)










