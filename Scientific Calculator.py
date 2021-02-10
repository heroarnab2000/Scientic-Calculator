#!/usr/bin/env python
# coding: utf-8


"""
Created by: Arnab Das
Date: 10-02-2021
Time: 03:16 PM

Feel free to use for academic purposes only.

"""


from tkinter import*
import math

me = Tk()
me.geometry("354x540")      #Specifies the default dimensions of the application
me.title("CALCULATOR")      #Name of the application

melabel = Label(me,text = "CALCULATOR",bg = 'grey',font = ("Times",30,'bold'))
melabel.pack(side=TOP)

me.config(background='Dark gray')

textin = StringVar()
operator=""
op = ""


try:
    def clickbut(number):
        global operator
        if number == 100:
            operator = operator + '00'
        elif number == '**':
            operator = operator + '^'
        else:
            operator = operator + str(number)
        textin.set(operator)

    def clickbutop(i):
        global op
        op = i
        clickbut(i)
        
    def clicksmallbut(func):
        global operator
        global op
        op = ""
        operator = ""
        operator = func + ' ' + operator
        textin.set(operator)

    def equlbut():
        global operator
        global op
        s = 0
        l = operator.find(op)
        s = operator.find(' ')
        
        if op == "+":
            n1 = operator[:l]
            n2 = operator[l+1:]
            res = float(n1) + float(n2)
        
        elif op == "-":
            n1 = operator[:l]
            n2 = operator[l+1:]
            res = float(n1) - float(n2)
        
        elif op == "*":
            n1 = operator[:l]
            n2 = operator[l+1:]
            res = float(n1) * float(n2)
        
        elif op == "/":
            n1 = operator[:l]
            n2 = operator[l+1:]
            res = float(n1) / float(n2)
        
        elif op == "**":
            n1 = operator[:operator.find('^')]
            n2 = operator[operator.find('^') + 1:]
            res = int(n1) ** int(n2)
        
        elif s:
            f = operator[:s]
            n1 = operator[s+1:]
            
            if f == 'asin':
                res = round(math.degrees(math.asin(float(n1))), 2)
            
            elif f == 'sin':
                res = round(math.sin(float(22 / (7 * (180 / float(n1))))), 2)
            
            elif f == 'acos':
                res = round(math.degrees(math.acos(float(n1))), 2)
            
            elif f == 'cos':
                res = round(math.cos(float(22 / (7 * (180 / float(n1))))), 2)
            
            elif f == 'atan':
                res = round(math.degrees(math.atan(float(n1))), 2)
            
            elif f == 'tan':
                res = round(math.tan(float(22 / (7 * (180 / float(n1))))), 2)
            
            elif f == 'log':
                res = round(math.log10(float(n1)), 2)
        
        textin.set(res)
        operator = str(res)

    def clrbut():
        global operator
        operator=""
        textin.set('')
        
except:
    operator=""
    textin.set('Syntax Error')

    
"""
This 'Entry' object is used dynamically to show operation as well as the result.

"""


metext = Entry(me,font=("Courier New",20,'bold'),textvar = textin,width=40,bd=5, bg = 'powder blue')
metext.pack()


"""
'Button' object is used to create different buttons on the calculator and calls the functions.
Buttons are placed by specifying the co-ordinates in the application.

"""


butasin = Button(me,padx=11,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('asin'),text="asin",font=("Courier New",8,'bold'))
butasin.place(x=10,y=110)

butsin = Button(me,padx=14,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('sin'),text="sin",font=("Courier New",8,'bold'))
butsin.place(x=10,y=145)

butacos = Button(me,padx=11,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('acos'),text="acos",font=("Courier New",8,'bold'))
butacos.place(x=75,y=110)

butcos = Button(me,padx=14,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('cos'),text="cos",font=("Courier New",8,'bold'))
butcos.place(x=75,y=145)

butatan = Button(me,padx=11,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('atan'),text="atan",font=("Courier New",8,'bold'))
butatan.place(x=140,y=110)

buttan = Button(me,padx=14,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('tan'),text="tan",font=("Courier New",8,'bold'))
buttan.place(x=140,y=145)

butlog = Button(me,padx=14,pady=3,bd=4,bg='dark turquoise',command=lambda:clicksmallbut('log'),text="log",font=("Courier New",8,'bold'))
butlog.place(x=205,y=110)

butpow = Button(me,padx=20,pady=2,bd=4,bg='dark turquoise',command=lambda:clickbutop('**'),text="^",font=("Courier New",10,'bold'))
butpow.place(x=205,y=145)

but1 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=320)

but2 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=75,y=320)

but3 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=140,y=320)

but4 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=10,y=250)

but5 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=250)

but6 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=140,y=250)

but7 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=10,y=180)

but8 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=75,y=180)

but9 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=180)

but0 = Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=390)

but00 = Button(me,padx=8,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut(100),text="00",font=("Courier New",16,'bold'))
but00.place(x=75,y=390)

butdot=Button(me,padx=47,pady=14,bd=4,bg='dark turquoise',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=140,y=390)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',text="/",command=lambda:clickbutop("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=180)

butmul=Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',text="*",command=lambda:clickbutop("*"),font=("Courier New",16,'bold'))
butmul.place(x=205,y=250)

butsub=Button(me,padx=14,pady=14,bd=4,bg='dark turquoise',text="-",command=lambda:clickbutop("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=320)

butadd=Button(me,padx=20,pady=49,bd=4,bg='dark turquoise',text="+",command=lambda:clickbutop("+"),font=("Courier New",16,'bold'))
butadd.place(x=270,y=320)

butclear=Button(me,padx=14,pady=49,bd=4,bg='dark turquoise',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=180)

butoff=Button(me,padx=8,pady=14,bd=4,bg='dark turquoise',text="OFF",command=me.destroy,font=("Courier New",16,'bold'))
butoff.place(x=270,y=110)

butequal=Button(me,padx=151,pady=14,bd=4,bg='dark turquoise',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=460)


me.mainloop()
