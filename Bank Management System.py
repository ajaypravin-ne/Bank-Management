import mysql.connector as bank
con = bank.connect(
    host='localhost',
    user='root',
    password='arise',
    database='pbi'
)
cur = con.cursor()

cur.execute('select * from customer_info')
detail = cur.fetchall()
one = list(detail[0])
two = list(detail[1])

from tkinter import ttk
from datetime import datetime
import tkinter
from tkinter import messagebox
import random
import string
from tkinter import PhotoImage
import pygame

mk = tkinter.Tk()
mk.title('Login')
mk.geometry('713x435+300+150')

frame = tkinter.Frame(bg='light slate grey')
mk.resizable(False, False)

frame.place(width=330, height=435, anchor='nw')

ima = PhotoImage(file="I:\\tleft.png")
photo = tkinter.Label(frame, image=ima)
photo.place(x=0, y=0, relwidth=1, relheight=1)

pho = tkinter.Frame()
pho.place(width=383, height=435, x=329, y=0)

imag = PhotoImage(
    file="I:\\WhatsApp Image 2024-09-02 at 20.50.31_5b503896.png"
)
photo1 = tkinter.Label(pho, image=imag)
photo1.pack()


def capcha():          # for capcha
    global c

    x = str(random.randint(0, 9))
    y = str(random.randint(0, 9))
    z = str(random.randint(0, 9))

    alphasmall = random.choice(string.ascii_lowercase)
    nalphasmall = random.choice(string.ascii_lowercase)
    ALPHABIG = random.choice(string.ascii_uppercase)
    alphabig = random.choice(string.ascii_uppercase)

    k = [x, y, z, alphasmall, nalphasmall, ALPHABIG, alphabig]

    c = ''

    for i in range(7):
        choice = random.choice(k)
        c += choice
        k.remove(choice)

    return c


def temperory(e):      # for showing how to write a account number
    entry.config()
    entry.delete(0, 'end')


def show_butt():       # for showing password
    pygame.mixer.music.load("show.mp3")
    pygame.mixer.music.play(loops=0)

    see.config(text='hide', command=hidbut)
    pasentry.config(show='')


def hidbut():          # for hiding password
    pygame.mixer.music.load("show.mp3")
    pygame.mixer.music.play(loops=0)

    pasentry.config(show='*')
    see.config(text='show', command=show_butt)


capcha()


def m():               # for message display
    x = entry.get()
    y = pasentry.get()

    if (x, y, c) == (one[0], one[3], capchaentry.get()):
        mk.destroy()
        next_page()
    else:
        messagebox.showerror(
            'Loginerror',
            'either your Account Number \n or Password or capcha \n '
            'dose not match'
        )


entry = tkinter.Entry(
    frame,
    font="Broadway",
    bg='gray9',
    fg='white',
    cursor='Hand1'
)
entry.place(x=20, y=120, width=250, height=20)


def buttoninentry(event):
    entry.config(
        background='grey30',
        foreground='white'
    )


def buttonoutentry(event):
    entry.config(
        background='grey9',
        foreground='white'
    )


entry.bind('<Enter>', buttoninentry)
entry.bind('<Leave>', buttonoutentry)


def buttoninpaswordentry(event):
    global displayx

    pasentry.config(
        background='grey30',
        foreground='white'
    )

    displayx = tkinter.Label(
        frame,
        text='*Must be 8 Characters*',
        background='grey9',
        foreground='white',
        font='system'
    )
    displayx.place(x=50, y=230)


def buttonoutpaswordentry(event):
    pasentry.config(
        background='grey9',
        foreground='white'
    )
    displayx.destroy()


def click(event):
    try:
        displayx.destroy()
    except tkinter.TclError:
        pass


pasentry = tkinter.Entry(
    frame,
    show='*',
    bg='gray9',
    fg='white',
    cursor='Hand1',
    font='Forte'
)
pasentry.place(x=20, y=200, width=250)

pasentry.bind('<Enter>', buttoninpaswordentry)
pasentry.bind('<Leave>', buttonoutpaswordentry)
pasentry.bind('<FocusIn>', click)

mk.title('Login')

pygame.mixer.init()


def loginplay():
    pygame.mixer.music.load("login.mp3")
    pygame.mixer.music.play(loops=0)


def comlogin():
    loginplay()
    m()


butt = tkinter.Button(
    frame,
    text='login',
    command=comlogin,
    bg='gray9',
    fg='white',
    cursor='Hand1',
    font='Terminal'
)
butt.place(x=100, y=370, width=100)


def buttoninbutt(event):
    butt.config(
        background='grey30',
        foreground='white'
    )


def buttonoutbutt(event):
    butt.config(
        background='grey9',
        foreground='white'
    )


butt.bind('<Enter>', buttoninbutt)
butt.bind('<Leave>', buttonoutbutt)


capchalable = tkinter.Label(
    frame,
    text=c,
    font="Garamond",
    bg='grey15',
    fg='lightgreen',
    cursor='Hand1'
)
capchalable.place(x=20, y=290, width=250)

capchaentry = tkinter.Entry(
    frame,
    bg='gray9',
    fg='white',
    cursor='Hand1',
    font='Helvetica'
)
capchaentry.place(x=20, y=320, width=250)


def buttonincapchaentry(event):
    capchaentry.config(
        background='grey30',
        foreground='white'
    )


def buttonoutcapchaentry(event):
    capchaentry.config(
        background='gray9',
        foreground='white'
    )


capchaentry.bind('<Enter>', buttonincapchaentry)
capchaentry.bind('<Leave>', buttonoutcapchaentry)

entry.insert(0, ' Account Number ')
entry.bind('<FocusIn>', temperory)

see = tkinter.Button(
    frame,
    text=" show ",
    command=show_butt,
    bg='gray9',
    fg='white',
    cursor='Hand1',
    font=('Terminal', 11)
)
see.place(y=201, x=271, width=45)


def buttoninsee(event):
    see.config(
        background='grey30',
        foreground='white'
    )


def buttonoutsee(event):
    see.config(
        background='grey9',
        foreground='white'
    )


see.bind('<Enter>', buttoninsee)
see.bind('<Leave>', buttonoutsee)

con.close()


def next_page():       # moves from login page to home page

    root = tkinter.Tk()
    root.config(bg='blue')
    root.state('zoomed')
    root.resizable(False, False)
    root.geometry('1369x768+0+0')
    root.title('bank')

    def help_page():
        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        allimg()

        global image
        image = tkinter.PhotoImage(file="I:\\helpbg.png")

        help_ = tkinter.Label(head, image=image)
        help_.place(x=0, y=0, relwidth=1, relheight=1)

        root.after(100000000000000, help_page)

    def expand():

        global hometxt
        global withdrawtxt
        global viewbalancetxt
        global transactiontxt
        global change_mpintxt
        global helptxt

        pygame.mixer.music.load("dot.mp3")
        pygame.mixer.music.play(loops=0)

        menu.config(command=shrink)
        option.config(width=210)
        head.config(width=1710)

        menuimg.config(file="I:\\line.png")
        menu.place(x=10, y=10)

        hometxt = tkinter.Label(
            option,
            text='Home',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        hometxt.place(y=85, x=90)

        withdrawtxt = tkinter.Label(
            option,
            text='Withdraw',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        withdrawtxt.place(y=165, x=90)

        viewbalancetxt = tkinter.Label(
            option,
            text='View\n Balance',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        viewbalancetxt.place(y=265, x=90)

        transcationtxt = tkinter.Label(
            option,
            text='Transcation',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        transcationtxt.place(y=360, x=80)

        change_mpintxt = tkinter.Label(
            option,
            text='Change\n Mpin',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        change_mpintxt.place(y=450, x=90)

        helptxt = tkinter.Label(
            option,
            text='HELP',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        helptxt.place(y=680, x=90)

        change_histxt = tkinter.Label(
            option,
            text='Transcation\n History',
            font=('Elephant', 14),
            bg='black',
            fg='white'
        )
        change_histxt.place(y=525, x=80)

    def shrink():

        pygame.mixer.music.load("dot.mp3")
        pygame.mixer.music.play(loops=0)

        menu.config(command=expand)
        menuimg.config(file="I:\\dot.png")
        menu.place(x=5, y=10)

        option.config(width=80)
        head.config(width=1840)

        hometxt.destroy()
        withdrawtxt.destroy()

    option = tkinter.Frame(
        root,
        bg='black',
        width=80,
        height=46
    )
    option.pack(side=tkinter.LEFT, fill=tkinter.Y)
    option.pack_propagate(False)

    head = tkinter.Frame(
        root,
        bg='blue',
        width=1840,
        height=100
    )
    head.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    head.pack_propagate(False)

    print(head.winfo_height())

    global menuimg
    menuimg = tkinter.PhotoImage(file="I:\\dot.png")

    menu = tkinter.Button(
        option,
        image=menuimg,
        command=expand,
        bg='black',
        activebackground='black',
        borderwidth=0
    )
    menu.place(x=0, y=10)

    def allimg():

        global change_image
        global vari

        change_image = [
            tkinter.PhotoImage(file="I:\\homeimg.png"),
            tkinter.PhotoImage(file="I:\\homeimg1.png"),
            tkinter.PhotoImage(file="I:\\homeimg2.png")
        ]

        vari = random.choice(change_image)

        homeimg = tkinter.Label(
            head,
            image=vari
        )
        homeimg.place(x=0, y=0, relwidth=1, relheight=1)

    var = 0

    root.after(2500, allimg)
    allimg()

    def home_fun():
        allimg()

    def balance():

        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        con = bank.connect(
            host='localhost',
            user='root',
            password='arise',
            database='pbi'
        )

        cur = con.cursor()
        cur.execute('use pbi')
        cur.execute('select * from customer_info')

        detail = cur.fetchall()
        one = list(detail[0])
        two = list(detail[1])

        global img1

        img1 = tkinter.PhotoImage(file="I:\\balanceimg.png")

        balanceimg = tkinter.Label(
            head,
            image=img1
        )
        balanceimg.place(x=0, y=0, relwidth=1, relheight=1)

        accno = tkinter.Entry(
            head,
            width=90,
            bg='darkslategray1',
            font=('Elephant', 16)
        )
        accno.place(x=350, y=290, height=30, width=350)

        mpin = tkinter.Entry(
            head,
            width=90,
            bg='darkslategray1',
            font=('Elephant', 16)
        )
        mpin.place(x=335, y=428, height=30, width=350)

        root.after(100000000000000, balance)

        bal = tkinter.Label(
            head,
            text='',
            width=30,
            bg='darkslategray1',
            fg='black',
            font=(30,)
        )
        bal.place(x=795, y=320, height=30, width=150)

        def show():

            pygame.mixer.music.load("enter.mp3")
            pygame.mixer.music.play(loops=0)

            if [accno.get(), int(mpin.get())] == [one[0], one[2]]:
                bal.config(text=one[4])
                con.close()
            else:
                messagebox.showerror('Wrong Entry')

        global enter3img

        enter3img = tkinter.PhotoImage(file="I:\\enter3.png")

        e3i = tkinter.Label(image=enter3img)

        enter = tkinter.Button(
            head,
            image=enter3img,
            command=show,
            border=0
        )
        enter.place(x=800, y=600)

        global homeimage

        homeimage = tkinter.PhotoImage(
            file="I:\\icons8-home-64.png"
        )

        home = tkinter.Button(
            option,
            image=homeimage,
            borderwidth=0,
            bg='black',
            activebackground='black',
            command=home_fun
        )
        home.place(x=20, y=85)

    def With():

        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        con = bank.connect(
            host='localhost',
            user='root',
            password='arise',
            database='pbi'
        )

        cur = con.cursor()
        cur.execute('use pbi')
        cur.execute('select * from customer_info')

        detail = cur.fetchall()
        one = list(detail[0])
        two = list(detail[1])

        global draw

        draw = tkinter.PhotoImage(file="I:\\with.png")

        drawn = tkinter.Label(
            head,
            image=draw
        )
        drawn.place(x=0, y=0, relwidth=1, relheight=1)

        root.after(100000000000000, With)

        accentry = tkinter.Entry(
            head,
            font=('Elephant', 16),
            bg='darkslategray1',
            fg='black'
        )
        accentry.place(x=295, y=225)

        mpinentry = tkinter.Entry(
            head,
            font=('Elephant', 16),
            bg='darkslategray1',
            fg='black'
        )
        mpinentry.place(x=290, y=370)

        ammount = tkinter.Entry(
            head,
            font=('Elephant', 16),
            bg='darkslategray1',
            fg='black'
        )
        ammount.place(x=280, y=500)

        def enter():

            pygame.mixer.music.load("enter.mp3")
            pygame.mixer.music.play(loops=0)

            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

            x = accentry.get().strip()
            y = int(mpinentry.get())
            am = ammount.get()

            if [str(one[0]), one[2]] == [x, y]:

                cur.execute(
                    'update customer_info set Balance=Balance-%s '
                    'where Acc_no=%s',
                    (am, x)
                )

                cur.execute(
                    'insert into p147258369147258 values(%s,%s,%s,%s)',
                    (
                        "--",
                        int(ammount.get()),
                        "debit",
                        formatted_date
                    )
                )

                con.commit()
                con.close()

                x = str(random.randint(0, 10))
                x1 = str(random.randint(0, 10))
                x2 = str(random.randint(0, 10))
                x3 = str(random.randint(0, 10))
                x4 = str(random.randint(0, 10))

                xf = x + x1 + x2 + x3 + x4

                messagebox.showinfo(
                    'Success',
                    'Withdraw successfull'
                )

                messagebox.showinfo(
                    'Success',
                    'Enter this pin in the nearest ATM'
                )

                messagebox.showinfo(
                    'Success',
                    xf
                )

                con.close()

            else:
                messagebox.showerror(
                    'Wrong Entry',
                    'wrong entry'
                )

        global enter3img

        enter3img = tkinter.PhotoImage(file="I:\\enter3.png")
        e3i = tkinter.Label(image=enter3img)

        entry = tkinter.Button(
            head,
            image=enter3img,
            command=enter,
            border=0
        )
        entry.place(x=800, y=600)

    def changempin():

        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        con = bank.connect(
            host='localhost',
            user='root',
            password='arise',
            database='pbi'
        )

        cur = con.cursor()
        cur.execute('use pbi')
        cur.execute('select * from customer_info')

        detail = cur.fetchall()
        one = list(detail[0])
        two = list(detail[1])

        global draw1

        draw1 = tkinter.PhotoImage(file="I:\\mpinimg.png")

        drawn = tkinter.Label(
            head,
            image=draw1
        )
        drawn.place(x=0, y=0, relwidth=1, relheight=1)

        root.after(100000000000000, changempin)

        mpinentry = tkinter.Entry(
            head,
            bg='darkslategray1',
            borderwidth=0,
            fg='black',
            font=('Elephant', 14)
        )
        mpinentry.place(x=385, y=296, height=30, width=400)

        ammount = tkinter.Entry(
            head,
            bg='darkslategray1',
            borderwidth=0,
            fg='black',
            font=('Elephant', 14)
        )
        ammount.place(x=385, y=435, height=30, width=400)

        def enter():

            pygame.mixer.music.load("enter.mp3")
            pygame.mixer.music.play(loops=0)

            am = mpinentry.get()
            x = ammount.get()

            print(am)
            print(one[2])

            if int(one[2]) == int(am):

                cur.execute(
                    'update customer_info set mpin=%s where mpin=%s',
                    (x, am)
                )

                con.commit()
                con.close()

                messagebox.showinfo(
                    'Success',
                    'M-Pin Changed Successfully'
                )

                con.close()

            else:
                messagebox.showerror(
                    'Wrong Entry',
                    'Wrong Entry'
                )

        global enter3img

        enter3img = tkinter.PhotoImage(file="I:\\enter3.png")
        e3i = tkinter.Label(image=enter3img)

        entry = tkinter.Button(
            head,
            image=enter3img,
            command=enter,
            border=0
        )
        entry.place(x=800, y=600)

    def transcation():

        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        con = bank.connect(
            host='localhost',
            user='root',
            password='arise',
            database='pbi'
        )

        cur = con.cursor()
        cur.execute('use pbi')
        cur.execute('select * from customer_info')

        detail = cur.fetchall()
        one = list(detail[0])
        two = list(detail[1])

        global draw2

        draw2 = tkinter.PhotoImage(file="I:\\transcationimg.png")

        drawn = tkinter.Label(
            head,
            image=draw2
        )
        drawn.place(x=0, y=0, relwidth=1, relheight=1)

        root.after(100000000000000, With)

        accentry = tkinter.Entry(
            head,
            font=('Elephant', 14),
            bg='darkslategray1',
            fg='black'
        )
        accentry.place(x=280, y=225)

        mpinentry = tkinter.Entry(
            head,
            font=('Elephant', 14),
            bg='darkslategray1',
            fg='black'
        )
        mpinentry.place(x=285, y=370)

        ammount = tkinter.Entry(
            head,
            font=('Elephant', 14),
            bg='darkslategray1',
            fg='black'
        )
        ammount.place(x=280, y=500)

        def enter():

            pygame.mixer.music.load("enter.mp3")
            pygame.mixer.music.play(loops=0)

            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

            x = accentry.get().strip()
            y = int(mpinentry.get())
            am = ammount.get()

            if [str(x), one[2]] == [x, y]:

                cur.execute(
                    'update customer_info set Balance=Balance - %s '
                    'where Acc_no="p147258369147258"',
                    (am,)
                )

                cur.execute(
                    'update customer_info set Balance=Balance+ %s '
                    'where Acc_no="p123456789123456"',
                    (am,)
                )

                cur.execute(
                    'insert into p147258369147258 '
                    'values(%s,%s,%s,%s)',
                    (
                        "p123456789123456",
                        int(ammount.get()),
                        "transcation out",
                        formatted_date
                    )
                )

                cur.execute(
                    'insert into p123456789123456 '
                    'values(%s,%s,%s,%s)',
                    (
                        "--",
                        int(ammount.get()),
                        "transcation in",
                        formatted_date
                    )
                )

                con.commit()

                messagebox.showinfo(
                    'Success',
                    'Transcation Successfull'
                )

                con.close()

            else:
                messagebox.showerror(
                    'Wrong Entry',
                    'Wrong Entry'
                )

        global enter3img

        enter3img = tkinter.PhotoImage(file="I:\\enter3.png")
        e3i = tkinter.Label(image=enter3img)

        entry = tkinter.Button(
            head,
            image=enter3img,
            command=enter,
            border=0
        )
        entry.place(x=800, y=600)

    def historyofyou():

        pygame.mixer.music.load("all.mp3")
        pygame.mixer.music.play(loops=0)

        global img1x

        img1x = tkinter.PhotoImage(file="I:\\histron.png")

        balanceimg = tkinter.Label(
            head,
            image=img1x
        )
        balanceimg.place(x=0, y=0, relwidth=1, relheight=1)

        con = bank.connect(
            host='localhost',
            user='root',
            password='arise',
            database='pbi'
        )

        cur = con.cursor()

        cur.execute(
            'select * from p147258369147258 '
            'order by date_time desc limit 10'
        )

        detail = cur.fetchall()

        one = list(detail[0])
        one2 = list(detail[1])
        one3 = list(detail[2])
        one4 = list(detail[3])
        one5 = list(detail[4])
        one6 = list(detail[5])
        one7 = list(detail[6])
        one8 = list(detail[7])
        one9 = list(detail[8])
        one10 = list(detail[9])

        table = ttk.Treeview(
            head,
            height=20,
            columns=(
                ' Transaction Account ',
                ' Amount ',
                ' Mode ',
                'Date_Time '
            ),
            show='headings'
        )

        table.heading(
            ' Transaction Account ',
            text=' Transaction Account '
        )

        table.heading(
            ' Amount ',
            text=' Amount '
        )

        table.heading(
            ' Mode ',
            text=' Mode '
        )

        table.heading(
            'Date_Time ',
            text='Date_Time '
        )

        table.insert(parent='', index=0, values=one)
        table.insert(parent='', index=2, values=one2)
        table.insert(parent='', index=4, values=one3)
        table.insert(parent='', index=6, values=one4)
        table.insert(parent='', index=8, values=one5)
        table.insert(parent='', index=10, values=one6)
        table.insert(parent='', index=12, values=one7)
        table.insert(parent='', index=14, values=one8)
        table.insert(parent='', index=16, values=one9)
        table.insert(parent='', index=18, values=one10)

        table.insert(parent='', index=1, values=['', '', '', ''])
        table.insert(parent='', index=3, values=['', '', '', ''])
        table.insert(parent='', index=5, values=['', '', '', ''])
        table.insert(parent='', index=7, values=['', '', '', ''])
        table.insert(parent='', index=9, values=['', '', '', ''])
        table.insert(parent='', index=11, values=['', '', '', ''])
        table.insert(parent='', index=13, values=['', '', '', ''])
        table.insert(parent='', index=15, values=['', '', '', ''])
        table.insert(parent='', index=17, values=['', '', '', ''])

        table.place(x=355, y=165)

        root.after(100000000000000, With)

        con.close()

    global withdrawimage

    withdrawimage = tkinter.PhotoImage(file="I:\\withdraw.png")

    withdraw = tkinter.Button(
        option,
        image=withdrawimage,
        borderwidth=0,
        bg='black',
        activebackground='black',
        command=With
    )
    withdraw.place(x=20, y=165)

    global balanceimg

    balanceimg = tkinter.PhotoImage(file="I:\\balance.png")

    balance = tkinter.Button(
        option,
        image=balanceimg,
        bg='black',
        activebackground='black',
        borderwidth=0,
        command=balance
    )
    balance.place(x=20, y=265)

    global transcationimg

    transcationimg = tkinter.PhotoImage(
        file="I:\\transcation.png"
    )

    transcation = tkinter.Button(
        option,
        image=transcationimg,
        bg='black',
        activebackground='black',
        borderwidth=0,
        command=transcation
    )
    transcation.place(x=20, y=360)

    global mpinimg

    mpinimg = tkinter.PhotoImage(file="I:\\mpin.png")

    mpin = tkinter.Button(
        option,
        image=mpinimg,
        bg='black',
        activebackground='black',
        borderwidth=0,
        command=changempin
    )
    mpin.place(x=20, y=450)

    global supportimg

    supportimg = tkinter.PhotoImage(file="I:\\support.png")

    support = tkinter.Button(
        option,
        image=supportimg,
        bg='black',
        activebackground='black',
        borderwidth=0,
        command=help_page
    )
    support.place(x=20, y=680)

    global historyimg

    historyimg = tkinter.PhotoImage(file="I:\\history.png")

    history = tkinter.Button(
        option,
        image=historyimg,
        bg='black',
        activebackground='black',
        borderwidth=0,
        command=historyofyou
    )
    history.place(x=20, y=525)

    mk.mainloop()
