from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_DEFAULT = ("Arial", 20, "italic")
FONT_SCORE = ("Courrier", 10, "bold")


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Computer Quizz")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Hello", font=(FONT_DEFAULT), fill=THEME_COLOR)

        self.score = Label(text="Score:0", font=(FONT_SCORE),
                           bg=THEME_COLOR, padx=20, pady=20, fg="white")
        self.score.grid(column=1, row=0)

        right_pic = PhotoImage(file="d33/images/true.png")
        self.right = Button(image=right_pic, highlightthickness=0,
                            command=self.show_check_answer_right)
        self.right.grid(column=1, row=2)

        wrong_pic = PhotoImage(file="d33/images/false.png")
        self.wrong = Button(image=wrong_pic, highlightthickness=0,
                            command=self.show_check_answer_wrong)
        self.wrong.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(
                self.question_text, text="You have completed the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def show_check_answer_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def show_check_answer_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000,  self.get_next_question)
