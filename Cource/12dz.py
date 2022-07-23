##1
##s = '8' * 70
##while '2222' in s or '8888' in s:
##    if '2222' in s:
##        s = s.replace('2222', '88', 1)
##    else:
##        s = s.replace('8888', '22', 1)
##print(s)

##2
##s = '2' + '5' * 81
##while '25' in s or '355' in s or '4555' in s:
##    if '25' in s:
##        s = s.replace('25', '4', 1)
##    if '355' in s:
##        s = s.replace('355', '2', 1)
##    if '4555' in s:
##        s = s.replace('4555', '3', 1)
##print(s)

##3
##s = '1' + '0' * 33
##while '1' in s or '100' in s:
##    if '100' in s:
##        s = s.replace('100', '0001', 1)
##    else:
##        s = s.replace('1', '00', 1)
##print(s.count('0'))

##4
##s = '1' * 46 + '2' * 31
##while '1111' in s:
##    s = s.replace('1111', '2', 1)
##    s = s.replace('222', '1', 1)
##print(s)

##5
##for i in range(1, 51):
##    s = '6' * i
##    while '66' in s:
##        s = s.replace('66', '1', 1)
##        s = s.replace('11', '2', 1)
##        s = s.replace('22', '6', 1)
##    if s == '21':
##        print(i)

##6
##s = '>' + '1' * 11 + '2' * 12 + '3' * 30
##print(s)
##while '>1' in s or '>2' in s or '>3' in s:
##    if '>1' in s:
##        s = s.replace('>1', '22>', 1)
##    if '>2' in s:
##        s = s.replace('>2', '2>', 1)
##    if '>3' in s:
##        s = s.replace('>3', '1>', 1)
##
##s = s[:-1]
##print(s)
##print(sum(int(x) for x in s))

##7
##s = '03'
##while '01' in s or '02' in s or '03' in s:
##    s = s.replace('01', '302', 1)
##    s = s.replace('02', '3103', 1)
##    s = s.replace('03', '20', 1)
##print(s)

##8
##s = '1121121121121111'
##while '11' in s:
##    if '112' in s:
##        s = s.replace('112', '7', 1)
##    else:
##        s = s.replace('11', '3', 1)
##print(sum(int(d) for d in s))

##9
##s = '9992' * 33 + '2' * 15 + '1' * 14 + '9'
##while '999' in s or '22' in s:
##    if '999' in s:
##        s = s.replace('999', '12', 1)
##    else:
##        s = s.replace('22', '1', 1)
##print(s.count('1'))

##10
##g = set()
##for x in range(1, 20):
##    
##    s = '5' * x
##    while '555' in s or '888' in s:
##        s = s.replace('555', '8', 1)
##        s = s.replace('888', '55', 1)
##    print(s)
##    g.add(s)
##print(len(g))

##19
##k = 1
##a = 'КАРА'
##i = len(a)
##b = 'T'
##while i > 1:
##    c = a[i - 1]
##    b = b + c
##    i = i - k
##print(b)

##20
##a = 'ИНФОРМАТИКА'
##m = 10
##b = a[m-1]
##for k in 4, 5:
##    c = a[k - 1]
##    b += c
##for x in 1, 2, 3:
##    c = a[x - 1]
##    b += c
##print(b)
b 
