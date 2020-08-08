import itertools
import random
from random import randint
from time import sleep
def printCardFromDeck(randonNum, myDeck, randonNum1):
    i = myDeck[randonNum]
    y = myDeck[randonNum1]
    print("Your cards are a {RANK} of {SUIT} and a {rank} of {suit}.\n\n".format(RANK = i[0], SUIT = i[1], rank = y[0], suit = y[1]))
suit = ['Spades', 'Diamonds', 'Hearts', 'Clovers']
suit_numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = list(itertools.product(suit_numbers, suit))
random.shuffle(deck)
a = 0
b = 1
printCardFromDeck(a,deck, b)
c = 2
d = 3
comp1 = deck[c]
comp2 = deck[d]
p = deck[a]
o = deck[b]
e = deck[4]
l = deck[5]
x = deck[6]
u = deck[7] 
z = deck[8]
if e[0] == 'Ace':
    m = 14
elif e[0] == 'King':
    m = 13
elif e[0] == 'Queen':
    m = 12
elif e[0] == 'Jack':
    m = 11
else:
    m = int(e[0])
if l[0] == 'Ace':
    n = 14
elif l[0] == 'King':
    n = 13
elif l[0] == 'Queen':
    n = 12
elif l[0] == 'Jack':
    n = 11
else:
    n = int(l[0])
if x[0] == 'Ace':
    s = 14
elif x[0] == 'King':
    s = 13
elif x[0] == 'Queen':
    s = 12
elif x[0] == 'Jack':
    s = 11
else:
    s = int(x[0])
if u[0] == 'Ace':
    f = 14
elif u[0] == 'King':
    f = 13
elif u[0] == 'Queen':
    f = 12
elif u[0] == 'Jack':
    f = 11
else:
    f = int(u[0])
if z[0] == 'Ace':
    v = 14
elif z[0] == 'King':
    v = 13
elif z[0] == 'Queen':
    v = 12
elif z[0] == 'Jack':
    v = 11
else:
    v = int(z[0])

sleep(3)
print("The first card on the table is a {RANK} of {SUIT}.".format(RANK = e[0], SUIT = e[1]))
print("The second card on the table is a {RANK} of {SUIT}.".format(RANK = l[0], SUIT = l[1]))
print("The third card on the table is a {RANK} of {SUIT}.".format(RANK = x[0], SUIT = x[1]))
sleep(3)
print("The fourth card on the table is a {RANK} of {SUIT}.".format(RANK = u[0], SUIT = u[1]))
sleep(2)
print("The fifth card on the table is a {RANK} of {SUIT}.".format(RANK = z[0], SUIT = z[1]))
sleep(2)
if p[0] == 'Ace':
    q = 14
elif p[0] == 'King':
    q = 13
elif p[0] == 'Queen':
    q = 12
elif p[0] == 'Jack':
    q = 11
else:
    q = int(p[0])
if o[0] == 'Ace':
    j = 14
elif o[0] == 'King':
    j = 13
elif o[0] == 'Queen':
    j = 12
elif o[0] == 'Jack':
    j = 11
else:
    j = int(o[0])
if comp1[0] == 'Ace':
    h = 14
elif comp1[0] == 'King':
    h = 13
elif comp1[0] == 'Queen':
    h = 12
elif comp1[0] == 'Jack':
    h = 11
else:
    h = int(comp1[0])
if comp2[0] == 'Ace':
    g = 14
elif comp2[0] == 'King':
    g = 13
elif comp2[0] == 'Queen':
    g = 12
elif comp2[0] == 'Jack':
    g = 11
else:
    g = int(comp2[0])
p1 = 0
p2 = 0
t = 0
k = 0
count = 0 
count1 = 0
count2 = 0
count3 = 0
if (((j == q) and (j == m))or((j == q) and (j == n))or((j == q) and (j == s))or((j == q) and (j == f))or((j == q) and (j == v))or((j == m) and (j == n))or((j == m) and (j == s))or((j == m) and (j == f))or((j == m) and (j == v))or((j == n) and (j == s))or((j == n) and (j == f))or((j == n) and (j == v))or((j == s) and (j == f))or((j == s) and (j == v))or((j == f) and (j == v))):
    p2 += 5
    p2 += j/100
    count2 = 1
if (((q == m) and (q == n))or((q == m) and (q == s))or((q == m) and (q == f))or((q == m) and (q == v))or((q == n) and (q == s))or((q == n) and (q == f))or((q == n) and (q == v))or((q == s) and (q == f))or((q == s) and (q == v))or((q == f) and (j == v))):
    p2 += 5
    p2 += j/100
    count2 = 1
if (((g == h) and (g == m))or((g == h) and (g == n))or((g == h) and (g == s))or((g == h) and (g == f))or((j == q) and (j == v))or((j == m) and (j == n))or((j == m) and (j == s))or((j == m) and (j == f))or((j == m) and (j == v))or((j == n) and (j == s))or((j == n) and (j == f))or((j == n) and (j == v))or((j == s) and (j == f))or((j == s) and (j == v))or((j == f) and (j == v))):
    p2 += 5
    p2 += j/100
    count3 = 1
if (((j == q) and (j == m))or((j == q) and (j == n))or((j == q) and (j == s))or((j == q) and (j == f))or((j == q) and (j == v))or((j == m) and (j == n))or((j == m) and (j == s))or((j == m) and (j == f))or((j == m) and (j == v))or((j == n) and (j == s))or((j == n) and (j == f))or((j == n) and (j == v))or((j == s) and (j == f))or((j == s) and (j == v))or((j == f) and (j == v))):
    p2 += 5
    p2 += j/100
    count3 = 1
if count2 == 0:
    if j == m:
        p2 += 2
        p2 += j/100
        count = 1
    if j == n:
        p2 += 2
        p2 += j/100
        count = 1
    if j == s:
        p2 += 2
        p2 += j/100
        count = 1
    if j == f:
        p2 += 2
        p2 += j/100
        count = 1
    if j == v:
        p2 += 2
        p2 += j/100
        count = 1
    if j == q:
        p2 += 2
        p2 += j/100
        count = 1
    if q == m:
        p2 += 2
        p2 += q/100
        count = 1
    if q == n:
        p2 += 2
        p2 += q/100
        count = 1
    if q == s:
        p2 += 2
        p2 += q/100
        count = 1
    if q == f:
        p2 += 2
        p2 += q/100
        count = 1
    if q == v:
        p2 += 2
        p2 += q/100
        count = 1
if count3 == 0:
    if g == m:
        p1 += 2
        p1 += g/100
        count1 = 1
    if g == n:
        p1 += 2
        p1 += g/100
        count1 = 1
    if g == s:
        p1 += 2
        p1 += g/100
        count1 = 1
    if g == f:
        p1 += 2
        p1 += g/100
        count1 = 1
    if g == v:
        p1 += 2
        p1 += g/100
        count1 = 1
    if g == h:
        p1 += 2
        p1 += g/100
        count1 = 1
    if h == m:
        p1 += 2
        p1 += h/100
        count1 = 1
    if h == n:
        p1 += 2
        p1 += h/100
        count1 = 1
    if h == s:
        p1 += 2
        p1 += h/100
        count1 = 1
    if h == f:
        p1 += 2
        p1 += h/100
        count1 = 1
    if h == v:
        p1 += 2
        p1 += h/100
        count1 = 1
if count1 == 0:
    if g > j:
        if g > q:
            p1 += g/100
        if g == q:
            if h > q:
                if h > j:
                    p1 += g/100
                    t = 1
    if g > q:
        if g > j:
            p1 += g/100
        if g == j:
            if h > j:
                if h > q:
                    p1 += g/100
                    t = 1

    if ((t == 0) and (h > j)):
        if h > q:
            p1 += h/100
        if h == q:
            if h > j:
                p1 += h/100
                t = 1

    if ((t == 0) and (h > q)):
        if h > j:
            p1 += h/100
        if h == j:
            if h > j:
                p1 += h/100
                t = 1
if count == 0:
    if q > g:
        if q > h:
            p2 += q/100
        if q == h:
            if j > g:
                p2 += q/100
                k = 1

    if q > h:
        if q > g:
            p2 += q/100
        if q == g:
            if q > h:
                p2 += q/100
                k = 1
    if ((k == 0) and (q > g)):
        if j > h:
            p2 += j/100
        if j == h:
            if q > g:
                p2 += j/100
                k = 1

    if ((k == 0) and (j > h)):
        if j > g:
            p2 += j/100
        if j == g:
            if q > g:
                p2 += j/100
                k = 1






sleep(3)
print("show cards in")
sleep(1)
print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
print("Your opponent's card is a {RANK} of {SUIT}".format(RANK = comp1[0], SUIT = comp1[1]))
print("Your opponent's card is a {RANK} of {SUIT}".format(RANK = comp2[0], SUIT = comp2[1]))
sleep(1)

if p1 > p2:
    print("\n\n\nThe computer wins.\n\n\n", p1, p2)

if p2 > p1:
    print("\n\n\nYou Win!\n\n\n", p1, p2)

if p1 == p2:
    if (((q == h) and (j == g)) and ((q == g) and (j == h))):
        print("\n\n\n Tie!\n\n\n", p1, p2)
    if (((q == h) and (j > g)) or ((q > g) and (j == h))):
        print("\n\n\n You Win!\n\n\n")
    if (((q > h) and (j == g)) or ((q == g) and (j > h))):
        print("\n\n\n You Win!\n\n\n")
    if (((h > q) and (j == g)) or ((q == g) and (h > j))):
        print("\n\n\n The computer Wins!\n\n\n")
    if (((q == h) and (g > j)) or ((g > q) and (j == h))):
        print("\n\n\n The computer Wins!\n\n\n")

