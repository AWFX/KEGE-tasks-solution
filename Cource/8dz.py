##1
##from itertools import product as f
##k = 0
##for x in f('КРСЛ', 'КРЕСЛО', 'КРЕСЛО', 'ЕО'):
##    k += 1
##print(k)

##2
##from itertools import product as f
##k = 0
##for x in f('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ'):
##    s = ''.join(x)
##    k += 1
##print(k)

##3
##from itertools import product as f
##k = 0
##for x in f('ПУЛЯ', repeat = 6):
##    s=''.join(x)
##    if s.count('У') == 2:
##        k +=1
##print(k)

##4
##from itertools import product as f
##k = 0
##for x in f('ЛОДКА', repeat = 4):
##    s=''.join(x)
##    if s.count('О') >= 2:
##        k += 1
##print(k)

##5
##from itertools import product as f
##k = 0
##for x in f('САЛО', repeat = 6):
##    s = ''.join(x)
##    if 1 <= s.count('О') <= 3:
##        k += 1
##print(k)

##6
##from itertools import permutations as f
##k = 0
##for x in f('ИГРОК'):
##    s = ''.join(x)
##    if s[0] != 'К' and not('РОК' in s):
##        k += 1
##print(k)

##7
##from itertools import permutations as f, product as g
##
##wrong = [''.join(x) for x in g('АИОУ', repeat=2)] + [''.join(x) for x in g('БКЛН',repeat=2)]
##k = 0
##for x in f('АБИКОЛУН'):
##    s=''.join(x)
##    if all(sub not in s for sub in wrong):
##        k += 1
##print(k)

##8
##from itertools import product as f
##k = 0
##for x in f('AB123',repeat=8):
##    s=''.join(x)
##    if s.count('A') + s.count('B') == 2:
##        k += 1
##print(k)

##9
##from itertools import product as f
##k = 0
##for x in f('234','01234','01234','01234','01234', '012'):
##    k += 1
##print(k)

##10
##from itertools import product as f
##k = 0
##for x in f('ВШНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВИШНЯ', 'ВШН'):
##    s=''.join(x)
##    if s.count('В') <= 1:
##        k += 1
##print(k)

##11
##from itertools import product as f
##k = 0
##for x in f('ABCD',repeat=4):
##    s=''.join(x)
##    if s[0] <= s[1] <= s[2] <=s[3]:
##        k += 1
##print(k)

##12
##from itertools import product as d
##k = 0
##for x in d('ГЕПАРД',repeat = 5):
##    s = ''.join(x)
##    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
##        k+=1
##print(k)

##13
##from itertools import product as h
##k = 0
##for x in h('0123456789', repeat=3):
##    s=''.join(x)
##    print(s)
##    if s[0] <= s[1] <= s[2] and s[0] != '0':
##        k+=1
##print(k)

##14
##from itertools import permutations as j
##true = ['ЙД', 'ЙК', 'ЙС', 'ЙТ', 'ЙР']
##k = 0
##for x in j('ДЕЙКСТРА',r = 6):
##    s=''.join(x)
##    if s.count('Й') == 1:
##        if any(sub in s for sub in true):
##            k += 1
##print(k)

##15
##from itertools import permutations as k
##wrong = ['ВФ', 'ФВ']
##S = 0
##for x in k('ВАЙФУ', r=4):
##    s = ''.join(x)
##    if s[0] != 'Й':
##        if all(not b in s for b in wrong):
##            S += 1
##print(S)

##16
##from itertools import permutations as j
##a = set()
##for x in j('МИМИКРИЯ'):
##    s = ''.join(x)
##    a.add(s)
##print(len(a))

##17
##from itertools import product as f
##k = 0
##for x in f('ЕЛМРУ',repeat = 4):
##    s = ''.join(x)
##    k += 1
##    if s[0] == 'Л':
##        print(k)

##18
##from itertools import product as h
##k = 0
##for x in h('АГИЛМОРТ',repeat = 4):
##    k+=1
##    s = ''.join(x)
##    if s[-2] + s[-1] == 'ИМ':
##        print(k)

##19
##from itertools import product as h
##k = 0
##for x in h('АИМРЯ', repeat = 4):
##    k += 1
##    s=''.join(x)
##    if s == 'АРИЯ':
##        print(k)

##20
##from itertools import product as l
##k = 0
##for x in l('АИМРЯ',repeat=4):
##    k += 1
##    s=''.join(x)
##    if k == 211:
##        print(s)
    
