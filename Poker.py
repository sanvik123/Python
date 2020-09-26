chip = 10000
chip1 = 10000
pot = 0
got = 0
print("Your balance is", chip)
while True:
    while True:  
        pot = 0
        print("entree fee of 50") 
        if input("Do you want to play?    ") == 'yes':
            chip -= 50
            chip1-= 50
            pot += 100 
            print("Your balance is", chip)
            import itertools
            import random
            from random import randint
            from time import sleep
            def printCardFromDeck(randonNum, myDeck, randonNum1):
                global deck
                global a
                global b
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
            p = deck[0] 
            o = deck[1] 
            e = deck[5] 
            l = deck[6] 
            x = deck[7] 
            u = deck[9] 
            z = deck[11]
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
            c3 = 0
            c4 = 0
            c5 = 0
            rand = randint(1, 6)
            rand2 = randint(1, 6)
            rand3 = randint(1, 6)
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
            count = -1 
            count1 = -1
            count2 = -1
            count3 = -1
            count4 = -1
            count5 = -1
            count6 = -1
            count7 = -1
            suit1 = [p[1], o[1], e[1], l[1], x[1], u[1], z[1]]
            suit2 = [comp1[1], comp2[1], e[1], l[1], x[1], u[1], z[1]]
            rank1 = [q, j, m, n, s, f, v]
            rank2 = [g, h, m, n, s, f, v]
            if j == 14:
                myrank1 = 1
                rank1.append(myrank1)
            if q == 14:
                myrank2 = 1
                rank1.append(myrank2)
            if m == 14:
                myrank3 = 1
                rank1.append(myrank3)
            if n == 14:
                myrank4 = 1
                rank1.append(myrank4)
            if s == 14:
                myrank5 = 1
                rank1.append(myrank5)
            if f == 14:
                myrank6 = 1
                rank1.append(myrank6)
            if v == 14:
                myrank7 = 1
                rank1.append(myrank7)
            if g == 14:
                their_rank1 = 1
                rank2.append(their_rank1)
            if h == 14:
                their_rank2 = 1
                rank2.append(their_rank2)
            if m == 14:
                trank3 = 1
                rank2.append(trank3)
            if n == 14:
                trank4 = 1
                rank2.append(trank4)
            if s == 14:
                trank5 = 1
                rank2.append(trank5)
            if f == 14:
                trank6 = 1
                rank2.append(trank6)
            if v == 14:
                trank7 = 1
                rank2.append(trank7)
            count8 = -1
            count9 = -1
            count10 = -1
            count11 = -1
            count12 = -1
            count13 = -1
            count14 = -1
            count15 = -1
            count16 = -1
            count17 = -1
            count18 = 0
            count19 = 0
            def RoyalFlush1():
                global p2
                global count16
                global count18
                global suit1
                global rank1
                if count18 == 0:
                    if ((rank1.__contains__(10) and rank1.__contains__(10 + 1) and rank1.__contains__(10 + 2) and rank1.__contains__(10+3) and rank1.__contains__(10+4)) and ((suit2.count("Spades") == 5) or (suit2.count("Diamonds") == 5) or (suit2.count("Hearts") == 5) or (suit2.count("CLovers") == 5))):
                        p2 += 60
                        p2 += max([j, q])/100
                        count16 = 1
                else:
                    count16 = 0
            def RoyalFlush2():
                global p1
                global count17
                global count19
                global suit2
                global rank2
                if count19 == 0:
                        if ((rank2.__contains__(10) and rank2.__contains__(10 + 1) and rank2.__contains__(10 + 2) and rank2.__contains__(10+3) and rank2.__contains__(10+4))) and ((suit2.count("Spades") == 5) or (suit2.count("Diamonds") == 5) or (suit2.count("Hearts") == 5) or (suit2.count("CLovers") == 5)):
                            p1 += 60
                            p1 += max([g, h])/100
                            count17 = 1
                else:
                    count17 = 0
            RoyalFlush1()
            RoyalFlush2()
            def StraightFlush2():
                global p1
                global count15
                global count17
                global suit2
                global rank2
                if count17 == 0:
                    for yot in range(1, 10):
                        if ((rank2.__contains__(yot) and rank2.__contains__(yot + 1) and rank2.__contains__(yot + 2) and rank2.__contains__(yot+3) and rank2.__contains__(yot+4))) and ((suit2.count("Spades") == 5) or (suit2.count("Diamonds") == 5) or (suit2.count("Hearts") == 5) or (suit2.count("CLovers") == 5)):
                            p1 += 50
                            p1 += max([g, h])/100
                            count15 = 1
                else:
                    count15 = 0
            def StraightFlush1():
                global p2
                global count14
                global count16
                global suit1
                global rank1
                if count16 == 0:
                    for toyu in range(1, 10):
                        if ((rank1.__contains__(toyu) and rank1.__contains__(toyu + 1) and rank1.__contains__(toyu + 2) and rank1.__contains__(toyu+3) and rank1.__contains__(toyu+4)) and ((suit2.count("Spades") == 5) or (suit2.count("Diamonds") == 5) or (suit2.count("Hearts") == 5) or (suit2.count("CLovers") == 5))):
                            p2 += 50
                            p2 += max([j, q])/100
                            count14 = 1
                else:
                    count14 = 0
            StraightFlush1()
            StraightFlush2()
            def F4():
                global p2
                global rank1
                global count12
                global count14
                if count14 == 0:
                    if rank1.count(q) == 4:
                        p2 += 40
                        p2 += q/100
                        count12 = 1
                    elif rank1.count(j) == 4:
                        p2 += 40
                        p2 += j/100
                        count12 = 1
                else:
                    count12 = 0
            def F4_1():
                global p1
                global rank2
                global count15
                global count13
                if count15 == 0:
                    if rank1.count(h) == 4:
                        p1 += 40
                        p1 += h/100
                        count13 = 1
                    elif rank1.count(g) == 4:
                        p1 += 40
                        p1 += g/100
                        count13 = 1
                else:
                    count13 = 0
            F4_1()
            F4()
            def fullhouse():
                global p2
                global count12
                global count10
                if count12 == 0:
                    if (((j == m) or (j == n) or (j == s)or (j == f)or (j == v)or (j == q)or (n == s)or (m == n)or (m == s)or (m == f)or (m == v)or (n == f)or (n == v)or (s == f)or (s == v)or (f == v))and((j == q) and (j == m))or((j == q) and (j == n))or((j == q) and (j == s))or((j == q) and (j == f))or((j == q) and (j == v))or((j == m) and (j == n))or((j == m) and (j == s))or((j == m) and (j == f))or((j == m) and (j == v))or((j == n) and (j == s))or((j == n) and (j == f))or((j == n) and (j == v))or((j == s) and (j == f))or((j == s) and (j == v))or((j == f) and (j == v))):
                        p2 += 30
                        p2 += j/100
                        count10 = 1
                    elif (((q == m) or (q == n) or (q == s)or (q == f)or (q == v)or (n == s)or (m == n)or (m == s)or (m == f)or (m == v)or (n == f)or (n == v)or (s == f)or (s == v)or (f == v))and ((q == m) and (q == n))or((q == m) and (q == s))or((q == m) and (q == f))or((q == m) and (q == v))or((q == n) and (q == s))or((q == n) and (q == f))or((q == n) and (q == v))or((q == s) and (q == f))or((q == s) and (q == v))or((q == f) and (q == v))):
                        p2 += 10
                        p2 += q/100
                        count10 = 1
                else:
                    count10 = 0
            def fullhouse2():
                global p1
                global count11
                global count13
                if count13 == 0:
                    if (((g == m) or (g == n) or (g == s)or (g == f)or (g == v)or (g == h)or (n == s)or (m == n)or (m == s)or (m == f)or (m == v)or (n == f)or (n == v)or (s == f)or (s == v)or (f == v))and(((g == h) and (g == m))or((g == h) and (g == n))or((g == h) and (g == s))or((g == h) and (g == f))or((g == h) and (g == v))or((g == m) and (g == n))or((g == m) and (g == s))or((g == m) and (g == f))or((g == m) and (g == v))or((g == n) and (g == s))or((g == n) and (g == f))or((g == n) and (g == v))or((g == s) and (g == f))or((g == s) and (g == v))or((g == f) and (g == v)))):
                        p1 += 30
                        p1 += g/100
                        count11 = 1
                    if (((h == m) or (h == n) or (h == s)or (h == f)or (h == v)or (n == s)or (m == n)or (m == s)or (m == f)or (m == v)or (n == f)or (n == v)or (s == f)or (s == v)or (f == v))and ((h == m) and (h == n))or((h == m) and (h == s))or((h == m) and (h == f))or((h == m) and (h == v))or((h == n) and (h == s))or((h == n) and (h == f))or((h == n) and (h == v))or((h == s) and (h == f))or((h == s) and (h == v))or((h == f) and (h == v))):
                        p1 += 30
                        p1 += h/100
                        count11 = 1
                else:
                    count11 = 0
            fullhouse()
            fullhouse2()
            def flush1():
                global p2
                global count8
                global count10
                global suit1
                global rank1
                if count10 == 1:
                    if ((suit1.count("Spades") == 5) or (suit1.count("Diamonds") == 5) or (suit1.count("Hearts") == 5) or (suit1.count("CLovers") == 5)):
                        p2 += 20
                        p2 += max([j, q])/100
                        count8 = 1
                else:
                    count8 = 0
            def flush2():
                global p1
                global count9
                global count11
                global suit2
                global rank2
                if count11 == 1:
                    if ((suit2.count("Spades") == 5) or (suit2.count("Diamonds") == 5) or (suit2.count("Hearts") == 5) or (suit2.count("CLovers") == 5)):
                        p1 += 20
                        p1 += max([g, h])/100
                        count9 = 1
                else:
                    count9 = 0
            flush1()
            flush2()
            def straight1():
                global p2
                global count6
                global count8
                global suit1
                global rank1
                if count8 == 0:
                    for i in range(1, 11):
                        if (rank1.__contains__(i) and rank1.__contains__(i + 1) and rank1.__contains__(i + 2) and rank1.__contains__(i+3) and rank1.__contains__(i+4)):
                            p2 += 10
                            p2 += max([j, q])/100
                            count6 = 1
                else:
                    count6 = 0
            def straight2():
                global p1
                global count7
                global count9
                global suit2
                global rank2
                if count9 == 0:
                    for o in range(1, 11):
                        if (rank2.__contains__(o) and rank2.__contains__(o + 1) and rank2.__contains__(o + 2) and rank2.__contains__(o+3) and rank2.__contains__(o+4)):
                            p1 += 10
                            p1 += max([g, h])/100
                            count7 = 1
                else:
                    count7 = 0
            straight1()
            straight2()
            def t3():
                global p2
                global count4
                global count2
                if count4 == 0:
                    if (((j == q) and (j == m))or((j == q) and (j == n))or((j == q) and (j == s))or((j == q) and (j == f))or((j == q) and (j == v))or((j == m) and (j == n))or((j == m) and (j == s))or((j == m) and (j == f))or((j == m) and (j == v))or((j == n) and (j == s))or((j == n) and (j == f))or((j == n) and (j == v))or((j == s) and (j == f))or((j == s) and (j == v))or((j == f) and (j == v))):
                        p2 += 5
                        p2 += j/100
                        count2 = 1
                    elif (((q == m) and (q == n))or((q == m) and (q == s))or((q == m) and (q == f))or((q == m) and (q == v))or((q == n) and (q == s))or((q == n) and (q == f))or((q == n) and (q == v))or((q == s) and (q == f))or((q == s) and (q == v))or((q == f) and (q == v))):
                        p2 += 5
                        p2 += q/100
                        count2 = 1
                else:
                    count2 = 0
            def Three_of_a_kind():
                global p1
                global count3
                global count5
                if count5 == 0:
                    if (((g == h) and (g == m))or((g == h) and (g == n))or((g == h) and (g == s))or((g == h) and (g == f))or((g == h) and (g == v))or((g == m) and (g == n))or((g == m) and (g == s))or((g == m) and (g == f))or((g == m) and (g == v))or((g == n) and (g == s))or((g == n) and (g == f))or((g == n) and (g == v))or((g == s) and (g == f))or((g == s) and (g == v))or((g == f) and (g == v))):
                        p1 += 5
                        p1 += g/100
                        count3 = 1
                    elif (((h == m) and (h == n))or((h == m) and (h == s))or((h == m) and (h == f))or((h == m) and (h == v))or((h == n) and (h == s))or((h == n) and (h == f))or((h == n) and (h == v))or((h == s) and (h == f))or((h == s) and (h == v))or((h == f) and (h == v))):
                        p1 += 5
                        p1 += h/100
                        count3 = 1
                else:
                    count3 = 0
            Three_of_a_kind()
            t3()
            def pair():
                global p2
                global count2
                global count
                if count2 == 0:
                    if j == m:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif j == n:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif j == s:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif j == f:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif j == v:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif j == q:
                        p2 += 2
                        p2 += j/100
                        count = 1
                    elif q == m:
                        p2 += 2
                        p2 += q/100
                        count = 1
                    elif q == n:
                        p2 += 2
                        p2 += q/100
                        count = 1
                    elif q == s:
                        p2 += 2
                        p2 += q/100
                        count = 1
                    elif q == f:
                        p2 += 2
                        p2 += q/100
                        count = 1
                    elif q == v:
                        p2 += 2
                        p2 += q/100
                        count = 1
                else:
                    count = 0
            def pair1():
                global p1
                global count1
                if count3 == 0:
                    if g == m:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif g == n:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif g == s:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif g == f:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif g == v:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif g == h:
                        p1 += 2
                        p1 += g/100
                        count1 = 1
                    elif h == m:
                        p1 += 2
                        p1 += h/100
                        count1 = 1
                    elif h == n:
                        p1 += 2
                        p1 += h/100
                        count1 = 1
                    elif h == s:
                        p1 += 2
                        p1 += h/100
                        count1 = 1
                    elif h == f:
                        p1 += 2
                        p1 += h/100
                        count1 = 1
                    elif h == v:
                        p1 += 2
                        p1 += h/100
                        count1 = 1
                else:
                    count1 = 0
            pair()
            pair1()
            def highcard():
                global count1
                global p1
                global t
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

                    if ((t == 0) and (h >= j)):
                        if h > q:
                            p1 += h/100
                        if h == q:
                                p1 += h/100
                                t = 1

                    if ((t == 0) and (h >= q)):
                        if h > j:
                            p1 += h/100
                        if h == j:
                                p1 += h/100
                                t = 1
            def highcard2():
                global count
                global p2
                global k
                if count == 0:
                    if q > g:
                        if q > h:
                            p2 += q/100
                        if q == h:
                                p2 += q/100
                                k = 1

                    if q > h:
                        if q > g:
                            p2 += q/100
                        if q == g:
                            if q > h:
                                p2 += q/100
                                k = 1
                    if ((k == 0) and (q >= g)):
                        if j > h:
                            p2 += j/100
                        if j == h:
                            if q > g:
                                p2 += j/100
                                k = 1

                    if ((k == 0) and (j >= h)):
                        if j > g:
                            p2 += q/100
                        if j == g:
                            if q > g:
                                p2 += q/100
                                k = 1
            highcard()
            highcard2()


            c6 = 0
            c7 = 0
            c8 = 0
            ct = 0
            ct1 = 0
            sleep(3)
            rand5 = randint(1,6)
            ra1 = randint(1,5)
            ra12 = randint(1,5)
            ra13 = randint(1,5)
            ra2 = randint(1,5)
            ra3 = randint(1,5)
            ra4 = randint(1,5)
            print("The first card on the table is a {RANK} of {SUIT}.".format(RANK = e[0], SUIT = e[1]))
            print("The second card on the table is a {RANK} of {SUIT}.".format(RANK = l[0], SUIT = l[1]))
            print("The third card on the table is a {RANK} of {SUIT}.".format(RANK = x[0], SUIT = x[1]))
            sleep(3)
            me = input("\nDo you want to continue? yes or no.\n").lower() 
            if me == 'no':
                print("")
                ct1 = 1
                break
            if me == 'm':
                chip += 500
            if input("\nDo you want to bet? yes or no.\n").lower() == 'yes':
                try:
                    bet = int(input("Enter the amount you want to bet.   "))
                except ValueError:
                    print("You have entered a invalid input. Run Again.\n")
                    break
                    break
                print('You bet', bet)
                chip -= bet
                pot += bet
                if chip < 0:
                    print("You have lost.")
                    ct1 = 1
                    break
                print("Your balance is", chip)
                if (p1 < p2) and ra1 < 3 :
                    print('Your opponent folded')
                    ct = 1
                    break
                else:
                    chip1 -= bet
                    pot += bet
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print('Your opponent called')
                    print("Your opponents balance is", chip1)
            if (p1 > p2) or ra2 > 2:
                if input("Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = 100).lower()) == ('no') :
                    chip1 -= 100
                    pot += 100
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("You folded")
                    ct1 = 1
                    break
                else:
                    chip1 -= 100
                    pot += 100
                    chip -= 100
                    pot += 100
                    if chip < 0:
                        print("You have lost.")
                        ct1 = 1
                        break
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("Your balance is", chip)
                    print("Your opponents balance is", chip1)
                    print('you called')
            print("The fourth card on the table is a {RANK} of {SUIT}.".format(RANK = u[0], SUIT = u[1]))
            sleep(2)
            if input("\nDo you want to continue? yes or no.\n").lower() == 'no':
                ct1 = 1
                break
            if input("\nDo you want to bet? yes or no.\n").lower() == 'yes':
                try:
                    bet1 = int(input("Enter the amount you want to bet.   "))
                except ValueError:
                    print("You have entered a invalid input. Run Again.\n")
                    break
                    break
                print('You bet', bet1)
                chip -= bet1
                pot += bet1
                if chip < 0:
                    print("You have lost.")
                    ct1 = 1
                    break
                print("Your balance is", chip)
                if (p1 < p2) or ra12 < 3:
                    print('Your opponent folded')
                    ct = 1
                    break
                else:
                    chip1 -= bet1
                    pot += bet1
                    if chip1 <= 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("Your opponent called")
                    print("Your opponents balance is", chip1)
            if (p1 > p2) or ra3 > 2:
                if input("Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = 100).lower()) == 'no':
                    chip1 -= 100
                    pot += 100
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("You folded")
                    ct1 = 1
                    break
                else:
                    chip1 -= 100
                    pot += 100
                    chip -= 100
                    pot += 100
                    if chip < 0:
                        print("You have lost.")
                        ct1 = 1
                        break
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("Your balance is", chip)
                    print("Your opponents balance is", chip1)
                    print('you called')
            print("The fifth card on the table is a {RANK} of {SUIT}.".format(RANK = z[0], SUIT = z[1]))
            sleep(2)
            if input("\nDo you want to continue? yes or no.\n").lower() == 'no':
                ct1 = 1
                break
            if input("\nDo you want to bet? yes or no.\n").lower() == 'yes':
                try:
                    bet2 = int(input("Enter the amount you want to bet.   "))
                except ValueError:
                    print("You have entered a invalid input. Run Again.\n")
                    break
                    break
                print('You bet', bet2)
                chip -= bet2
                pot += bet2
                if chip < 0:
                    print("You have lost.")
                    ct1 = 1
                    break
                print("Your balance is", chip)
                
                if (p1 < p2) and ra13 < 3:
                    print('Your opponent folded')
                    ct = 1
                    break
                else:
                    chip1 -= bet2
                    pot += bet2
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("Your opponent called")
                    print("Your opponents balance is", chip1)
            if (p1 > p2) or ra2 > 2:
                if input("Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = 100).lower()) == 'no':
                    chip1 -= 100
                    pot += 100
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("You folded")
                    ct1 = 1
                    break
                else:
                    chip1 -= 100
                    pot += 100
                    chip -= 100
                    pot += 100
                    if chip < 0:
                        print("You have lost.")
                        ct1 = 1
                        break
                    if chip1 < 0:
                        print("Your opponent has lost.")
                        ct = 1
                        break
                    print("Your balance is", chip)
                    print("Your opponents balance is", chip1)
                    print('you called')

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
                chip1 += pot
                print("\n\n\nThe computer wins.\n\n\n", p1, p2)
                print("Your opponents balance is", chip1)
                print("Your balance is", chip)
            if p2 > p1:
                chip += pot
                print("\n\n\nYou Win!\n\n\n", p1, p2)
                print("Your balance is", chip)
                print("Your opponents balance is", chip1)

            if p1 == p2:
                if (((q == h) and (j == g)) or ((q == g) and (j == h))):
                    print("\n\n\n Tie!\n\n\n", p1, p2)
                    print("Your balance is", chip, p1,p2)
                    print("Your opponents balance is", chip1, p1,p2)
                    chip += pot/2
                    chip1 = pot/2
                if (((q == h) and (j > g)) or ((q > g) and (j == h))):
                    chip += pot
                    print("\n\n\n You Win!\n\n\n", p1, p2)
                    print("Your balance is", chip, p1,p2)
                    print("Your opponents balance is", chip1, p1,p2)
                if (((q > h) and (j == g)) or ((q == g) and (j > h))):
                    chip += pot
                    print("\n\n\n You Win!\n\n\n", p1, p2)
                    print("Your balance is", chip, p1,p2)
                    print("Your opponents balance is", chip1, p1,p2)
                if (((h > q) and (j == g)) or ((q == g) and (h > j))):
                    chip1 += pot
                    print("\n\n\n The computer Wins!\n\n\n", p1, p2)
                    print("Your opponents balance is", chip1, p1,p2)
                    print("Your balance is", chip, p1,p2)
                if (((q == h) and (g > j)) or ((g > q) and (j == h))):
                    chip1 += pot
                    print("\n\n\n The computer Wins!\n\n\n", p1, p2)
                    print("Your opponents balance is", chip1, p1,p2)
                    print("Your balance is", chip, p1,p2)

    else:
        break
    if got == 0:
        if ct == 1:
            chip += pot
            print("\nYou Win\n", p1, p2)
            print("Your opponents balance is", chip1, p1,p2)
            print("Your balance is", chip, p1,p2)
        if ct1 == 1:
            chip1 += pot
            print("\nThe computer wins\n", p1, p2)
            print("Your opponents balance is", chip1, p1,p2)
            print("Your balance is", chip, p1,p2)
        pot = 0
        if chip <= 0:
            break
        if chip1 <= 0:
            break
ct = 1
ct1 = 1
if chip > chip1:
    print("\n\nYou win the game!\n\n")
    print("Your balance is", chip)
    print("Your opponents balance is", chip1)
if chip == chip1:
    print("\n\nTie!\n\n")
    print("Your balance is", chip)
    print("Your opponents balance is", chip1)
if chip1 > chip:
    print("\n\nYour opponent wins the game!\n\n")
    print("Your balance is", chip)
    print("Your opponents balance is", chip1)
