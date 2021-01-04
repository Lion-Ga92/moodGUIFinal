from tkinter import *
from tkinter import ttk
import sqlite3

class mood_Backend:

    def __init__(self):
        self = self

    def set_conn(self):
        f = 1

        self.conn = sqlite3.connect('mood_baro.db')

        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS moodBarometer ('emotions' TEXT,
                        'date' TEXT, 'day_Rate' INTEGER, 'mood_Rate' INTEGER, 'sleep_Rate' INTEGER,
                        'anxiety_Rate' INTEGER, 'depression_Rate' INTEGER, 'obsession_Rate' INTEGER,
                        'spiritual_Rate' INTEGER, 'hygiene_Rate' INTEGER, 'diet_Rate' INTEGER, workout_Rate INTEGER, 
                        'total' INTEGER, 'id code' INTEGER);""")
        
        self.conn.commit()

        while f != 1:
            self.conn.close()

    def add_Vals(self, a, b, r, d, e, x, h, i, j, k, l, m, n, p):
        self.a = a
        self.b = b
        self.r = r
        self.d = d
        self.e = e
        self.x = x
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.p = p
        self.c = self.conn.cursor()
        self.data = (a, b, r, d, e, x, h, i, j, k, l, m, n, p)
        self.query = "INSERT INTO moodBarometer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        self.c.execute(self.query, self.data)
        self.conn.commit()
        f = 1
    
    def confirm_Entry(self, a):    
        window_2 = Tk()
        frame_1 = Frame(window_2)
        frame_2 = Frame(window_2)
        frame_1.pack()
        frame_2.pack()
        lbl_one = Label(frame_1, text="Your values have been added to the database, you can close this app now!!")
        lbl_one.pack()     
        enter_button = Button(frame_2, text="Close", command=lambda : exit())
        enter_button.pack()









