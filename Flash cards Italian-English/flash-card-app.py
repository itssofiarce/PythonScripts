from tkinter import *
import pandas
import random
#--CONTS--#
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 60, "bold")
WORD_FONT = ("Arial", 40, "italic")
new_word_italian = {}
dict_of_words = {}

try:
    csv = pandas.read_csv("Flash cards Italian-English/data/italian_words.csv")
except:
    original_data = pandas.read_csv("d31/data/italian_words.csv")
    dict_of_words = original_data.to_dict(orient="records")
else:
    dict_of_words = csv.to_dict(orient="records")

#----GAME SETUP---#


def correct():
    dict_of_words.remove(new_word_italian)
    data = pandas.DataFrame(dict_of_words)
    data.to_csv("Flash cards Italian-English/data/to_learn.csv", index=False)
    to_check_answer()


def flip_card():  # flips the card to English
    # shows english card
    word_in_english = new_word_italian["English"]
    canvas.itemconfigure(italian_card, image=english_image)
    canvas.itemconfigure(word, text=f"{word_in_english}", fill="white")
    canvas.itemconfigure(title, text="English")
    window.after_cancel(to_check_answer)


def to_check_answer():  # shows italian card
    global new_word_italian, refresh
    window.after_cancel(refresh)
    new_word_italian = random.choice(dict_of_words)
    canvas.itemconfigure(word, text=new_word_italian["Italian"], fill="black")
    canvas.itemconfigure(title, text="Italian", fill="black")
    canvas.itemconfigure(italian_card, image=image)
    refresh = window.after(3000, func=flip_card)


#----UI SETUP---#
window = Tk()
window.title("Learn Italian")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

refresh = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0,)
image = PhotoImage(file="Flash cards Italian-English\images\card_front.png")
italian_card = canvas.create_image(400, 263, image=image)
english_image = PhotoImage(file="Flash cards Italian-English\images\card_back.png")
canvas.grid(column=1, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=(TITLE_FONT))
word = canvas.create_text(400, 263, text="", font=(WORD_FONT))


wrong_pic = PhotoImage(file="Flash cards Italian-English/images/wrong.png")
wrong = Button(image=wrong_pic, highlightthickness=0, command=to_check_answer)
wrong.grid(column=0, row=1)

right_pic = PhotoImage(file="Flash cards Italian-English/images/right.png")
right = Button(image=right_pic, highlightthickness=0, command=correct)
right.grid(column=1, row=1)

to_check_answer()
window.mainloop()
