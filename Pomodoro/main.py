from tkinter import *
from tkinter import messagebox
import math


PINK = "#EAA397"
RED = "#E7443C"
GREEN = "#A6A6DD"
YELLOW = "#FFE5DC"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60

reps = 0
timer_clock = None
#------------TIME RESET-------------#


def reset_timer():
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer_text, text="25:00")
    global reps
    reps = 0
    timer.config(text="Timer")
    check_mark.config(text="")


#------------TIMER MECHANISM-------------#


def start_timer():
    global reps
    reps += 1
    if reps >= 9:
        window.bell()
        keep_working = messagebox.askyesno(
            'Yes|No', 'Do you want to start again?')
        if not keep_working:
            window.destroy()
        reps = 1
        check_mark.config(text="")

    if reps % 8 == 0:
        timer.config(text="LONG BREAK", fg=RED)
        window.bell()
        messagebox.showinfo(
            'Good Job!', "Let's take a long break")
        countdown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer.config(text="SHORT BREAK", fg=PINK)
        window.bell()
        messagebox.showinfo(
            'Break Time!', 'Work time has finished. Time for a break')
        countdown(SHORT_BREAK_MIN)
    else:
        timer.config(text="WORK TIME")
        if reps > 2:
            window.bell()
        messagebox.showinfo(
            'Work Time!', "Let's work")
        countdown(WORK_MIN)


#------------COUNTDOWN MECHANISM-------------#
def pause():
    """It pauses whatever it is running"""

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec >= 0 and count_sec <= 9:
        count_sec = f"0{count_sec}"

    if count_min >= 0 and count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_clock
        timer_clock = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✔"
        check_mark.config(text=mark)


#------------UI SETUP-------------#
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)


#---column 0#
start = Button(text="START", font=(FONT_NAME, 22, "bold"),
               fg=GREEN, bg=YELLOW, highlightthickness=0, borderwidth=0, command=start_timer)
start.grid(column=0, row=2)
#---column 1#
timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"),
              fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1, row=0)

#--Pause button
pause = Label(text="PAUSE", font=(FONT_NAME, 22, "bold"),
               fg=GREEN, bg=YELLOW, highlightthickness=0, borderwidth=0, command=pause)
pause.grid(column=1, row=2)
#--

check_mark = Label(font=(FONT_NAME, 15, "bold"),
                   fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(145, 100, image=tom_img)
timer_text = canvas.create_text(146, 115, text="25:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#---column 2#
reset = Button(text="RESET", font=(FONT_NAME, 22, "bold"),
               fg=GREEN, bg=YELLOW, highlightthickness=0, borderwidth=0, command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()  # event driven they are constaly checking if something happened
