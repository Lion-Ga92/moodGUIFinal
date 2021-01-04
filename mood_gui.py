from sqlite3.dbapi2 import enable_callback_tracebacks
from tkinter import *
from tkinter import ttk
from datetime import date
from classes import mood_Backend
import random

back_end = mood_Backend()
back_end.set_conn()

root = Tk()
frame_1 = Frame(root)
frame_1.grid(row=1, column=1)
frame_2 = Frame(root)
frame_2.grid(row=2, column=1)
frame_3 = Frame(root, borderwidth=2, relief="raised")
frame_3.grid(row=3, column=1)
lbl_greet = Label(frame_1, text="Hello!!! Enter your three emotions:    ")
lbl_greet.grid(row=1, column=1)
ent_usr = Entry(frame_1, width="10")
ent_usr.grid(row=1, column=2)
ent_date = Entry(frame_1, width="10")
ent_date.grid(row=1, column=4)
lbl_date = Label(frame_1, text="Enter date: ")
lbl_date.grid(row=1, column=3)
#frame_2 widgets

lbl_day_stat = Label(frame_2, text="Good day- Bad day\n FOR THE VALUE SCALES 1=GOOD 3=STRESSED OUT 5=CRISIS IN CATEGORY")
lbl_day_stat.grid(row=1, column=1)

day_rate = IntVar()
day_scal = Scale(frame_2, orient=HORIZONTAL, variable=day_rate, length=500, from_="1", to="5")
day_scal.grid(row=2, column=1)

lbl_mood = Label(frame_2, text="Mood:", width="16")
lbl_mood.grid(row=3, column=1)

mood_rate = IntVar()
mood_scal = Scale(frame_2, orient=HORIZONTAL, length=500, variable=mood_rate, from_="1", to="5")
mood_scal.grid(row=4, column=1)


lbl_sleep = Label(frame_2, text="Sleep:", width="16")
lbl_sleep.grid(row=5, column=1)

sleep_rate = IntVar()
sleep_sc = Scale(frame_2, orient=HORIZONTAL, variable=sleep_rate, length=500, from_="1", to="5")
sleep_sc.grid(row=6, column=1)

lbl_anxiet = Label(frame_2, text="Anxiety:", width="16")
lbl_anxiet.grid(row=7, column=1)

anx_rate = IntVar()
scal_anx = Scale(frame_2, orient=HORIZONTAL, variable= anx_rate, length=500, from_="1", to="5")
scal_anx.grid(row=8, column=1)

lbl_depre = Label(frame_2, text="Depression:", width="16")
lbl_depre.grid(row=9, column=1)

depre_rate = IntVar()
depr_scal = Scale(frame_2, orient=HORIZONTAL, variable=depre_rate, length=500, from_="1", to="5")
depr_scal.grid(row=10, column=1)

lbl_obsess = Label(frame_2, text="Obessesion:", width="16")
lbl_obsess.grid(row=11, column=1)

obsess_rate = IntVar()
obsess_scal = Scale(frame_2, orient=HORIZONTAL, variable=obsess_rate, length=500, from_="1", to="5")
obsess_scal.grid(row=12, column=1)

lbl_spirit = Label(frame_2, text="Spirituality", width="16")
lbl_spirit.grid(row=13, column=1)

sprt_rate = IntVar()
sprt_scal = Scale(frame_2, orient=HORIZONTAL, variable=sprt_rate, length=500, from_="1", to="5")
sprt_scal.grid(row=14, column=1)

lbl_hygiea= Label(frame_2, text="Hygiene:", width="16")
lbl_hygiea.grid(row=15, column=1)

hygia_rate = IntVar()
hygiea_scal = Scale(frame_2, orient=HORIZONTAL, variable= hygia_rate, length=500, from_="1", to="5")
hygiea_scal.grid(row=16, column=1)

lbl_diet = Label(frame_2, text="diet:", width="16")
lbl_diet.grid(row=17, column=1)

diet_rate = IntVar()
diet_scal = Scale(frame_2, orient=HORIZONTAL, variable=diet_rate, length=500, from_="1", to="5")
diet_scal.grid(row=18, column=1)

lbl_exercise = Label(frame_2, text="Exercise:", width="16")
lbl_exercise.grid(row=19, column=1)

workout_rate = IntVar()
workout_scal = Scale(frame_2, orient=HORIZONTAL, variable=workout_rate, length=500, from_="1", to="5")
workout_scal.grid(row=20, column=1)

lbl_scale_mssg = Label(frame_2, text="score ratings: <20% You are having a good day!\n 20% >= you <= 50% You are stressed, but manageable. \n > 50% You are stressed out and risking a crisis \n 100% CRISIS!!! CALL SOMEONE")
lbl_scale_mssg.grid(row=21, column=1)

total_Vals = IntVar()
ent_totals = Entry(frame_2, widt=10)
ent_totals.grid(row=22, column=1)
total_Vals = ent_totals.get()

lbl_totals = Label(frame_2, text="Out of 50")
lbl_totals.grid(row=23, column=1)

def confirming_logs():
    emotions = ent_usr.get()
    date_gtr = ent_date.get()
    day_check = day_rate.get()
    mood_check = mood_rate.get()
    sleep_check = sleep_rate.get()
    anx_chec = anx_rate.get()
    depress_check = depre_rate.get()
    obsess_check = obsess_rate.get()
    sprt_check = sprt_rate.get()
    hygie_check = hygia_rate.get()
    diet_check = diet_rate.get()
    workout_check = workout_rate.get()
    tots_vals = ent_totals.get()
    id_code = random.randrange(0, 99999, 2)
    back_end.add_Vals(emotions, date_gtr, day_check, mood_check, sleep_check, anx_chec, depress_check, obsess_check, sprt_check, hygie_check, diet_check, workout_check, tots_vals, id_code)

bttn_ent1 = Button(frame_1, text="Sum up: ", command=lambda: ent_totals.insert(0, (int(day_rate.get()) + int(mood_rate.get()) + int(sleep_rate.get()) + int(anx_rate.get()) + int(depre_rate.get()) + int(obsess_rate.get()) + int(sprt_rate.get()) + int(hygia_rate.get()) + int(diet_rate.get()) + int(workout_rate.get()))))
bttn_ent1.grid(row=2, column=2)
btt_ent2 = Button(frame_1, text="add logs", command=confirming_logs)
btt_ent2.grid(row=2, column=3)
bttn_nxt = Button(frame_1, text="Confirm and close", command= lambda : back_end.confirm_Entry(total_Vals))
bttn_nxt.grid(row=2, column=4)

root.mainloop()

