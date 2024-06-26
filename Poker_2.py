import sys
import turtle
from time import sleep
from random import choice
from random import randint
import os
chip = 10000
chip1 = 10000
pot = 0
got = 1
some = (1/3)
wn = turtle.Screen()
wn.setup(1150, 1100)
cd = turtle.Turtle()
cd.hideturtle()
cd.speed(0)
cd.pensize(3)
cd.penup()
imports = {0:"Functions", 1:"Cards", 2:"Methods", 3:"Other Data"}
importtime = [6, 9, 12]
cd.write("A Poker Game by Sanvik Vangala", font = ('Courier', 35, 'italic'), align="center")
sleep(4)
cd.undo()
fd = turtle.Turtle()
fd.speed(0)
fd.penup()
fd.right(90)
fd.forward(50)
fd.right(-90)
fd.hideturtle()
fd.pensize(2)
fd.speed(0)
fd.penup()
fd.backward(100)
fd.forward(200)
fd.right(-90)
fd.pendown()
fd.forward(15)
fd.right(-90)
fd.penup()
fd.forward(200)
fd.right(-90)
fd.pendown()
fd.forward(15)
fd.right(-180)
fd.forward(7.5)
fd.right(90)
fd.pensize(10)
fd.speed(0)
fd.pendown()
fd.color("red")
fd.forward(200)
fd.penup()
fd.right(180)
fd.forward(200)
fd.right(180)
fd.pendown()
fd.color("lime green")
bd = 0
sleep(1)
wn.clear()
nd = turtle.Turtle()
nd1 = turtle.Turtle()
nd2 = turtle.Turtle()
nd.penup()
nd.hideturtle()
nd.forward(300)
nd1.penup()
nd1.hideturtle()
nd1.forward(300)
nd2.penup()
nd2.hideturtle()
nd2.forward(300)
md = turtle.Turtle()
md.penup()
md.hideturtle()
md.speed(0)
md.right(90)
md.forward(100)
md.write("Complete!", font = ('Courier', 35, 'italic'), align="center")
sleep(2)
md.undo()
nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
nd1.left(90)
nd2.left(90)
nd1.forward(50)
nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
nd2.forward(-50)
nd2.write("Oppenent Chips = {chip1}".format(chip1 = chip), font = ('Courier', 15, 'italic'), align="center")
hgw = True
while hgw:
    while hgw:
        pot = 0
        cardS = turtle.Turtle()
        cardS.hideturtle()
        cardS.penup()
        cardS.speed(0)
        cardS.goto(-240, -100)
        cardS.write("Your balance is {chip}".format(chip = chip), font = ('Courier', 20, 'italic'), align="center")
        sleep(2)
        cardS.undo()
        cardS.write(("Entree fee of 50"), font = ('Courier', 20, 'italic'), align="center")
        sleep(2)
        t11 = turtle.textinput("Choice", "Do you want to play?  y/n for all questions and numbers for bets  ")
        cardS.undo()
        if t11 == ('yes') or t11 == ('y'):
            chip -= 50
            chip1-= 50
            pot += 100
            nd.undo()
            nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
            nd1.undo()
            nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
            nd2.undo()
            nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
            print("Your balance is", chip)
            import itertools
            import random
            suit = ['Spades', 'Diamonds', 'Hearts', 'Clovers']
            suit_numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            deck = list(itertools.product(suit_numbers, suit))
            random.shuffle(deck)
            style = ('Courier', 30, 'italic')
            a = 0
            b = 1
            c = 2
            d = 3
            check_error = 0
            comp1 = deck[c]
            comp2 = deck[d]
            p = deck[0]
            o = deck[1]
            e = deck[5]
            l = deck[6]
            x = deck[7]
            u = deck[9]
            z = deck[11]
            card0 = turtle.Turtle()
            class Card:
                def __init__(self, suiter, card):
                    card.hideturtle()
                    card.penup()
                    card.speed(0)
                    card.pensize(3)
                    card.right(90)
                    card.forward(100)
                    card.pendown()
                    card.forward(100)
                    card.right(90)
                    card.forward(65)
                    card.right(90)
                    card.forward(100)
                    card.right(90)
                    card.forward(65)
                    card.penup()
                    card.forward(-65)
                    card.penup()
                    card.right(90)
                    card.forward(23)
                    card.right(-90)
                    card.forward(10)
                    if (suiter[1])[0] == "H":
                        card.color("red")
                    if (suiter[1])[0] == "S":
                        card.color("black")
                    if (suiter[1])[0] == "C":
                        card.color("green")
                    if (suiter[1])[0] == "D":
                        card.color("blue")
                    card.write("{suit}".format( suit = (suiter[1])[0]), font = ('Courier', 20, 'italic'), align="center")
                    card.right(90)
                    card.forward(50)
                    card.right(-90)
                    card.forward(20)
                    if (suiter[0]) == "10":
                        card.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
                    else:
                        card.write("{suit}".format( suit = (suiter[0])[0]), font = ('Courier', 50, 'italic'), align="center")
                    card.color("black")
            card1 = Card
            card1.__init__(p, p, card0)
            card2 = Card
            card0.right(90)
            card0.forward(-100)
            card0.right(-90)
            card0.goto(85, 0)
            card2.__init__(p, o, card0)
            #card2 = Card
            #card2.__init__(p, p, card0)
            mcard = turtle.Turtle()
            mcard.hideturtle()
            mcard.penup()
            mcard.speed(0)
            mcard.goto(0, 200)
            mcard.write("?",font = ('Courier', 100, 'italic'), align="center")
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
                    if max([g, h]) > max([j, q]):
                        p1 += 1
                        p1 += max([g, h])/100
            def highcard2():
                global count
                global p2
                global k
                if count == 0:
                    if max([j, q]) > max([g, h]):
                        p2 += 1
                        p2 += max([j, q])/100
            highcard()
            highcard2()


            c6 = 0
            c7 = 0
            c8 = 0
            ct = 0
            ct1 = 0
            sleep(3)
            rand5 = randint(1,6)
            ra1 = randint(1,6)
            ra12 = randint(1,6)
            ra13 = randint(1,6)
            ra2 = randint(1,5)
            ra3 = randint(1,5)
            ra4 = randint(1,5)
            cd = turtle.Turtle()
            cd.hideturtle()
            cd.speed(0)
            cd.pensize(3)
            cd.penup()
            cd.goto(0, 0)
            cd.forward(-200)
            cd.right(90)
            cd.penup()
            cd.forward(-100)
            cd.pendown()
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.penup()
            cd.forward(-65)
            cd.penup()
            cd.right(90)
            cd.forward(23)
            cd.right(-90)
            cd.forward(10)
            if (e[1])[0] == "H":
                cd.color("red")
            if (e[1])[0] == "S":
                cd.color("black")
            if (e[1])[0] == "C":
                cd.color("green")
            if (e[1])[0] == "D":
                cd.color("blue")
            cd.write("{suit}".format( suit = (e[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            cd.right(90)
            cd.forward(50)
            cd.right(-90)
            cd.forward(20)
            if (e[0]) == "10":
                cd.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                cd.write("{suit}".format( suit = (e[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            cd.color("black")
            cd.right(90)
            cd.goto(-125, 100)
            cd.pendown()
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.penup()
            cd.forward(-65)
            cd.penup()
            cd.right(90)
            cd.forward(23)
            cd.right(-90)
            cd.forward(10)
            if (l[1])[0] == "H":
                cd.color("red")
            if (l[1])[0] == "S":
                cd.color("black")
            if (l[1])[0] == "C":
                cd.color("green")
            if (l[1])[0] == "D":
                cd.color("blue")
            cd.write("{suit}".format( suit = (l[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            cd.right(90)
            cd.forward(50)
            cd.right(-90)
            cd.forward(20)
            if (l[0]) == "10":
                cd.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                cd.write("{suit}".format( suit = (l[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            cd.color("black")
            cd.right(90)
            cd.goto(-50, 100)
            cd.pendown()
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.penup()
            cd.forward(-65)
            cd.penup()
            cd.right(90)
            cd.forward(23)
            cd.right(-90)
            cd.forward(10)
            if (x[1])[0] == "H":
                cd.color("red")
            if (x[1])[0] == "S":
                cd.color("black")
            if (x[1])[0] == "C":
                cd.color("green")
            if (x[1])[0] == "D":
                cd.color("blue")
            cd.write("{suit}".format( suit = (x[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            cd.right(90)
            cd.forward(50)
            cd.right(-90)
            cd.forward(20)
            if (x[0]) == "10":
                cd.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                cd.write("{suit}".format( suit = (x[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            cd.color("black")
            print("The first card on the table is a {RANK} of {SUIT}.".format(RANK = e[0], SUIT = e[1]))
            print("The second card on the table is a {RANK} of {SUIT}.".format(RANK = l[0], SUIT = l[1]))
            print("The third card on the table is a {RANK} of {SUIT}.".format(RANK = x[0], SUIT = x[1]))
            sleep(3)
            def timer():
                    turt = turtle.Turtle()
                    turt.hideturtle()
                    turt.penup()
                    turt.speed(0)
                    turt.forward(50)
                    turt.left(90)
                    turt.forward(100)
                    turt.write(10, font = ('Courier', 50, 'italic'), align="center")
                    ui = 10
                    ci = 0
                    while True:
                        sleep(1)
                        ui -= 1
                        if ci > 0:
                            turt.undo()
                        ci += 1
                        turt.write(ui, font = ('Courier', 50, 'italic'))
                        if ui == 0:
                            break
            def quit():
                wn.bye()
            wn.listen(timer, "p")
            wn.listen(quit, "q")


















            me = turtle.textinput("Choice", "Do you want to continue?")
            if me == 'n':
                ct1 = 1
                got = 0
                break
            if me == 'm':
                chip += 500
            if turtle.textinput("Choice", "\nDo you want to bet? y or n.\n") == ('y' or "yes" or ''):
                while True:
                    try:
                        bet = turtle.textinput("Choice", "Enter the amount you want to bet.   ")
                        bett = int(bet)
                    except ValueError:
                        cd.goto(-240, -100)
                        cd.write(('Invalid Input, Try Again'.format(chiper = bet)), font = ('Courier', 15, 'italic'), align="center")
                        sleep(1)
                        cd.undo()
                    else:
                        break
                cd.goto(-240, -100)
                cd.write(('You bet {chiper}'.format(chiper = bet)), font = ('Courier', 15, 'italic'), align="center")
                sleep(1)
                cd.undo()
                chip -= bett
                pot += bett
                nd.undo()
                nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                nd1.undo()
                nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                wn.listen(timer, "p")
                wn.listen(quit, "q")
                if chip < 0:
                    cd.write(('You have lost'), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct1 = 1
                    got = 0
                    break
                cd.write(("Your balance is {chiper}".format(chiper = chip)), font = ('Courier', 15, 'italic'), align="center")
                sleep(2)
                cd.undo()
                cd.goto(-240, -100)
                wn.listen(timer, "p")
                wn.listen(quit, "q")
                if ((not((((bett<200) and p1 > 2) or ((bett>200 and bett<500) and p1 > 5) or ((bett>500 and bett<1000) and p1 > 10) or (((bett>1000) and bett<5000 )and p1 > 20)or ((bett>5000) and p1 > 30)))) and ra1 < 3) or (bett>chip1):
                    cd.write(("Your opponent folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    cd.goto(-240, -100)
                    ct = 1
                    got = 0
                    break
                else:
                    chip1 -= bett
                    pot += bett
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(('  Your opponent called.\n Your opponents balance\n is {chip1er}'.format(chip1er = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(3)
                    cd.undo()
            wn.listen(timer, "p")
            wn.listen(quit, "q")
            if (p1 > 2) and ra2 > 3:
                cd.goto(-240, -100)
                if not turtle.textinput("Choice", "Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = (int(p1)+1)*100)) == ("y" or'yes'):
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("You folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct1 = 1
                    got = 0
                    wn.listen(timer, "p")
                    wn.listen(quit, "q")
                    break
                else:
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    chip -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    cd.goto(-240, -100)
                    if chip < 0:
                        cd.write(("Your have lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct1 = 1
                        got = 0
                        break
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("Your balance is {some}.\n Your opponents balance\n is {some1}. You called.".format(some = chip, some1 = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(3)
                    cd.undo()
            wn.listen(timer, "p")
            wn.listen(quit, "q")
            cd.goto(25, 100)
            cd.pendown()
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.penup()
            cd.forward(-65)
            cd.penup()
            cd.right(90)
            cd.forward(23)
            cd.right(-90)
            cd.forward(10)
            if (u[1])[0] == "H":
                cd.color("red")
            if (u[1])[0] == "S":
                cd.color("black")
            if (u[1])[0] == "C":
                cd.color("green")
            if (u[1])[0] == "D":
                cd.color("blue")
            cd.write("{suit}".format( suit = (u[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            cd.right(90)
            cd.forward(50)
            cd.right(-90)
            cd.forward(20)
            if (u[0]) == "10":
                cd.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                cd.write("{suit}".format( suit = (u[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            cd.color("black")
            sleep(2)
            if turtle.textinput("Choice", "\nDo you want to continue? yes or no.\n") == ("n" or'no'):
                ct1 = 1
                got = 0
                break
            if turtle.textinput("Choice", "\nDo you want to bet? yes or no.\n").lower() == ('y' or "yes"):
                while True:
                    try:
                        bet1 = turtle.textinput("Choice", "Enter the amount you want to bet.   ")
                        bett1 = int(bet1)
                    except ValueError:
                        cd.goto(-240, -100)
                        cd.write(('Invalid Input, Try Again'.format(chiper = bet1)), font = ('Courier', 15, 'italic'), align="center")
                        sleep(1)
                        cd.undo()
                    else:
                        break
                cd.goto(-240, -100)
                cd.write(("You bet {chier}".format(chier = bet1)), font = ('Courier', 20, 'italic'), align="center")
                sleep(1)
                cd.undo()
                bett1 = int(bet1)
                chip -= bett1
                pot += bett1
                nd.undo()
                nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                nd1.undo()
                nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                cd.goto(-240, -100)
                if chip < 0:
                    cd.write(("You have lost"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    cd.goto(-240, -100)
                    ct1 = 1
                    got = 0
                    break
                print("Your balance is", chip)
                if ((not((((bett1<200) and p1 > 2) or ((bett1>200 and bett1<500) and p1 > 5) or ((bett1>500 and bett1<1000) and p1 > 10) or (((bett1>1000) and bett1<5000 )and p1 > 20)or ((bett1>5000) and p1 > 30)))) and ra12 < 3) or (bett1>chip1):
                    cd.write(("Your opponent folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct = 1
                    got = 0
                    break
                else:
                    chip1 -= bett1
                    pot += bett1
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 <= 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("Your opponent called.\n Your opponents balance\n is {cilper}".format(cilper = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
            if (p1 > 2) and ra3 > 2:
                cd.goto(-240, -100)
                if not turtle.textinput("Choice", "Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = (int(p1)+1)*100)) == ("y" or'yes'):
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("You folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    cd.goto(-240, -100)
                    ct1 = 1
                    got = 0
                    break
                else:
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    chip -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip < 0:
                        cd.write(("You have lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct1 = 1
                        got = 0
                        break
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("Your balance is {some2}.\n Your opponents balance\n is {some3}. You called.".format(some2 = chip, some3 = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(3)
                    cd.undo()
                    cd.goto(-240, -100)
            cd.goto(100, 100)
            cd.pendown()
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.right(90)
            cd.forward(100)
            cd.right(90)
            cd.forward(65)
            cd.penup()
            cd.forward(-65)
            cd.penup()
            cd.right(90)
            cd.forward(23)
            cd.right(-90)
            cd.forward(10)
            if (z[1])[0] == "H":
                cd.color("red")
            if (z[1])[0] == "S":
                cd.color("black")
            if (z[1])[0] == "C":
                cd.color("green")
            if (z[1])[0] == "D":
                cd.color("blue")
            cd.write("{suit}".format( suit = (z[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            cd.right(90)
            cd.forward(50)
            cd.right(-90)
            cd.forward(20)
            if (z[0]) == "10":
                cd.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                cd.write("{suit}".format( suit = (z[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            cd.color("black")
            sleep(2)
            sleep(2)
            cd.goto(-240, -100)
            if turtle.textinput("Choice", "\nDo you want to continue? yes or no.\n") == ("n" or'no'):
                ct1 = 1
                got = 0
                break
            if turtle.textinput("Choice", "\nDo you want to bet? yes or no.\n") == ('y' or "yes"):
                bet2 = turtle.textinput("Choice", "Enter the amount you want to bet.   ")
                while True:
                    try:
                        bet2 = turtle.textinput("Choice", "Enter the amount you want to bet.   ")
                        bett2 = int(bet2)
                    except ValueError:
                        cd.goto(-240, -100)
                        cd.write(('Invalid Input, Try Again'.format(chiper = bet2)), font = ('Courier', 15, 'italic'), align="center")
                        sleep(1)
                        cd.undo()
                    else:
                        break
                cd.write(('You bet {jkjk}'.format(jkjk = bet2)), font = ('Courier', 20, 'italic'), align="center")
                sleep(2)
                cd.undo()
                bett2 = int(bet2)
                chip -= bett2
                pot += bett2
                nd.undo()
                nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                nd1.undo()
                nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                if chip < 0:
                    cd.write('You have lost', font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct1 = 1
                    got = 0
                    break
                cd.write('Your balance is {some5}'.format(some5 = chip), font = ('Courier', 15, 'italic'), align="center")
                sleep(2)
                cd.undo()
                if ((not((((bett2<200) and p1 > 2) or ((bett2>200 and bett2<500) and p1 > 5) or ((bett2>500 and bett2<1000) and p1 > 10) or (((bett2>1000) and bett2<5000 )and p1 > 20)or ((bett2>5000) and p1 > 30)))) and ra13 < 3) or (bett2>chip1):
                    cd.write(("Your opponent folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct = 1
                    got = 0
                    break
                else:
                    chip1 -= bett2
                    pot += bett2
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("Your opponent called.\n Your opponents balance\n is {chip2}".format(chip2 = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(3)
                    cd.undo()
            if (p1 > 2) and ra2 > 2:
                cd.goto(-240, -100)
                if not turtle.textinput("Choice", "Your opponent bet {bet}. Do you want to call? yes or no.   ".format(bet = (int(p1)+1)*100)) == ("y" or'yes'):
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("You folded"), font = ('Courier', 15, 'italic'), align="center")
                    sleep(2)
                    cd.undo()
                    ct1 = 1
                    got = 0
                    break
                else:
                    chip1 -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    chip -= ((int(p1)+1)*100)
                    pot += ((int(p1)+1)*100)
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    if chip < 0:
                        cd.write(("You have lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct1 = 1
                        got = 0
                        break
                    if chip1 < 0:
                        cd.write(("Your opponent has lost"), font = ('Courier', 15, 'italic'), align="center")
                        sleep(2)
                        cd.undo()
                        ct = 1
                        got = 0
                        break
                    cd.write(("Your opponent called.\n Your opponents balance\n is {chip2}".format(chip2 = chip1)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(3)
                    cd.undo()

            cd.write(("Show Cards In"), font = ('Courier', 15, 'italic'), align="center")
            sleep(3)
            cd.undo()
            sleep(1)
            cd.write((3), font = ('Courier', 15, 'italic'), align="center")
            sleep(1)
            cd.undo()
            cd.write((2), font = ('Courier', 15, 'italic'), align="center")
            sleep(1)
            cd.undo()
            cd.write((1), font = ('Courier', 15, 'italic'), align="center")
            sleep(1)
            cd.undo()
            mcard.pendown
            mcard.undo()
            mcard.pensize(3)
            mcard.goto(-50, 250)
            mcard.right(90)
            mcard.pendown()
            mcard.forward(100)
            mcard.right(90)
            mcard.forward(65)
            mcard.right(90)
            mcard.forward(100)
            mcard.right(90)
            mcard.forward(65)
            mcard.penup()
            mcard.forward(-65)
            mcard.penup()
            mcard.right(90)
            mcard.forward(23)
            mcard.right(-90)
            mcard.forward(10)
            if (comp1[1])[0] == "H":
                mcard.color("red")
            if (comp1[1])[0] == "S":
                mcard.color("black")
            if (comp1[1])[0] == "C":
                mcard.color("green")
            if (comp1[1])[0] == "D":
                mcard.color("blue")
            mcard.write("{suit}".format( suit = (comp1[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            mcard.right(90)
            mcard.forward(50)
            mcard.right(-90)
            mcard.forward(20)
            if (comp1[0]) == "10":
                mcard.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                mcard.write("{suit}".format( suit = (comp1[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            mcard.color("black")
            mcard.right(90)
            mcard.goto(25, 250)
            mcard.pendown()
            mcard.forward(100)
            mcard.right(90)
            mcard.forward(65)
            mcard.right(90)
            mcard.forward(100)
            mcard.right(90)
            mcard.forward(65)
            mcard.penup()
            mcard.forward(-65)
            mcard.penup()
            mcard.right(90)
            mcard.forward(23)
            mcard.right(-90)
            mcard.forward(10)
            if (comp2[1])[0] == "H":
                mcard.color("red")
            if (comp2[1])[0] == "S":
                mcard.color("black")
            if (comp2[1])[0] == "C":
                mcard.color("green")
            if (comp2[1])[0] == "D":
                mcard.color("blue")
            mcard.write("{suit}".format( suit = (comp2[1])[0]), font = ('Courier', 20, 'italic'), align="center")
            mcard.right(90)
            mcard.forward(50)
            mcard.right(-90)
            mcard.forward(20)
            if (comp2[0]) == "10":
                mcard.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
            else:
                mcard.write("{suit}".format( suit = (comp2[0])[0]), font = ('Courier', 50, 'italic'), align="center")
            mcard.color("black")
            mcard.pendown()
            sleep(1)
            p1 = float(p1)
            p2 = float(p2)
            if p1 > p2:
                chip1 += pot
                cd.write(("\n\n\nThe computer wins {p1}, {p2}.\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
                sleep(4)
                cd.undo()
                wn.clear()
            elif p2 > p1:
                chip += pot
                cd.write(("\n\n\nYou win {p1}, {p2}.\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
                sleep(4)
                cd.undo()
                wn.clear()
            else:
                if (((q == h) and (j == g)) or ((q == g) and (j == h))):
                    cd.write(("\n\n\nTie {p1}, {p2}.\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(4)
                    cd.undo()
                    print("\n\n\n Tie!\n\n\n", p1, p2)
                    print("Your balance is", chip, p1,p2)
                    print("Your opponents balance is", chip1, p1,p2)
                    chip += pot/2
                    chip1 = pot/2
                    pot = 0
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    wn.clear()
                elif (max([j, q]) > max([g, h])):
                    chip += pot
                    pot = 0
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    cd.write(("\n\n\nYou win {p1}, {p2}.\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(4)
                    cd.undo()
                    wn.clear()
                else:
                    chip1 += pot
                    pot = 0
                    nd.undo()
                    nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
                    nd1.undo()
                    nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
                    nd2.undo()
                    nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
                    cd.write(("\n\n\nThe computer wins {p1}, {p2}.\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
                    sleep(4)
                    cd.undo()
                    wn.clear()
            cd.goto(-240, -100)
            for variable in range(12):
                    if variable % 3 == 0:
                        cd.write("Game Over. Loading Game Data.", font = ('Courier', 15, 'italic'), align="center")
                        sleep(some)
                        cd.undo()
                    elif variable % 3 == 1:
                        cd.write("Game Over. Loading Game Data..", font = ('Courier', 15, 'italic'), align="center")
                        sleep(some)
                        cd.undo()
                    elif variable % 3 == 2:
                        cd.write("Game Over. Loading Game Data...", font = ('Courier', 15, 'italic'), align="center")
                        sleep(some)
                        cd.undo()
            break
        else:
            wn.clear()
    elif:
        break
    if got == 0:
        mcard.undo()
        mcard.pensize(3)
        mcard.goto(-50, 250)
        mcard.right(90)
        mcard.pendown()
        mcard.forward(100)
        mcard.right(90)
        mcard.forward(65)
        mcard.right(90)
        mcard.forward(100)
        mcard.right(90)
        mcard.forward(65)
        mcard.penup()
        mcard.forward(-65)
        mcard.penup()
        mcard.right(90)
        mcard.forward(23)
        mcard.right(-90)
        mcard.forward(10)
        if (comp1[1])[0] == "H":
            mcard.color("red")
        if (comp1[1])[0] == "S":
            mcard.color("black")
        if (comp1[1])[0] == "C":
            mcard.color("green")
        if (comp1[1])[0] == "D":
            mcard.color("blue")
        mcard.write("{suit}".format( suit = (comp1[1])[0]), font = ('Courier', 20, 'italic'), align="center")
        mcard.right(90)
        mcard.forward(50)
        mcard.right(-90)
        mcard.forward(20)
        if (comp1[0]) == "10":
            mcard.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
        else:
            mcard.write("{suit}".format( suit = (comp1[0])[0]), font = ('Courier', 50, 'italic'), align="center")
        mcard.color("black")
        mcard.right(90)
        mcard.goto(25, 250)
        mcard.pendown()
        mcard.forward(100)
        mcard.right(90)
        mcard.forward(65)
        mcard.right(90)
        mcard.forward(100)
        mcard.right(90)
        mcard.forward(65)
        mcard.penup()
        mcard.forward(-65)
        mcard.penup()
        mcard.right(90)
        mcard.forward(23)
        mcard.right(-90)
        mcard.forward(10)
        if (comp2[1])[0] == "H":
            mcard.color("red")
        if (comp2[1])[0] == "S":
            mcard.color("black")
        if (comp2[1])[0] == "C":
            mcard.color("green")
        if (comp2[1])[0] == "D":
            mcard.color("blue")
        mcard.write("{suit}".format( suit = (comp2[1])[0]), font = ('Courier', 20, 'italic'), align="center")
        mcard.right(90)
        mcard.forward(50)
        mcard.right(-90)
        mcard.forward(20)
        cd.goto(-240, -100)
        if (comp2[0]) == "10":
            mcard.write("{suit}".format( suit = "10"), font = ('Courier', 50, 'italic'), align="center")
        else:
            mcard.write("{suit}".format( suit = (comp2[0])[0]), font = ('Courier', 50, 'italic'), align="center")
        mcard.color("black")
        sleep(1)
        if ct == 1:
            chip += pot
            pot = 0
            nd.undo()
            nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
            nd1.undo()
            nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
            nd2.undo()
            nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
            cd.write(("\n\n\nYou win!\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
            sleep(4)
            cd.undo()
            wn.clear()
        elif ct1 == 1:
            chip1 += pot
            pot = 0
            nd.undo()
            nd.write("Pot = {Pot}".format(Pot = pot), font = ('Courier', 15, 'italic'), align="center")
            nd1.undo()
            nd1.write("Your Chips = {chip}".format(chip = chip), font = ('Courier', 15, 'italic'), align="center")
            nd2.undo()
            nd2.write("Opponent Chips = {chip1}".format(chip1 = chip1), font = ('Courier', 15, 'italic'), align="center")
            cd.write(("\n\n\n      The computer wins!\n\n\n      Your opponents balance\n    is {win}. Your balance\n    is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
            sleep(4)
            cd.undo()
            wn.clear()
        cd.goto(-240, -100)
        for variable in range(12):
            if variable % 3 == 0:
                cd.write("Game Over. Loading Game Data.", font = ('Courier', 15, 'italic'), align="center")
                sleep(.3)
                cd.undo()
            elif variable % 3 == 1:
                cd.write("Game Over. Loading Game Data..", font = ('Courier', 15, 'italic'), align="center")
                sleep(.3)
                cd.undo()
            elif variable % 3 == 2:
                cd.write("Game Over. Loading Game Data...", font = ('Courier', 15, 'italic'), align="center")
                sleep(.3)
                cd.undo()
        if chip <= 0:
            break
        if chip1 <= 0:
            break
ct = 1
ct1 = 1
if chip > chip1:
    cd.write(("\n\nYou win the game!\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
    sleep(4)
    cd.undo()
    sys.exit()
if chip == chip1:
    cd.write(("\n\nTie!\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
    sleep(4)
    cd.undo()
    sys.exit()
if chip1 > chip:
    cd.write(("\n\n\nThe computer wins!\n\n\nYour opponents balance\n is {win}.Your balance\n is {lose}".format(p1 = p1, p2 = p2, win = chip1, lose = chip)), font = ('Courier', 15, 'italic'), align="center")
    sleep(4)
    cd.undo()
    sys.exit()
wn.mainloop()
