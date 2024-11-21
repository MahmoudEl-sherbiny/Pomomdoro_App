import math
from tkinter import *

BLUE = "#384B70"
WHITE = "#FCFAEE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Functions
# start function that is related with start button
def start():
    """run the timer and determined which session of sessions i have """
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # take care about arrangement of if conditions
    if reps % 8 == 0:
        count_down(long_break_sec)
        # we want to change label of timer label to know this is a long break
        timer_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break")
    else:
        count_down(work_sec)
        timer_label.config(text="Work")

def count_down(count):

    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    # change the  timer text
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        # .after function it work as loop that is call specific function with argument after amount of time in ms
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_mark_label.config(text=mark)

# reset function related with reset button
def reset():
    """Stop the timer and return with this format 00:00 """
    # by using .after_cancel() to stop after function
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps  # Focus on global well
    reps = 0


# Create a window and put your painting(board) inside it
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=BLUE)



# Create your painting with width and height and background color and remove border
canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)


tomato_img = PhotoImage(file="tomato.png")
# Put your image inside your painting with x, y coordinates
canvas.create_image(100, 112, image=tomato_img)
# Put This format "00:00" on a background image with x, y coordinates
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)
# you must call this function after created canvas object
# count_down(5*60)

# Labels--->(Timer and modify on it to be Work Session , Short break Session , Long break Session) , Sign of Check Mark
# Timer
timer_label = Label(text="Timer", fg=WHITE, bg=BLUE, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

# check mark
check_mark_label = Label(fg="white", bg=BLUE, font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(row=3, column=1)


# Buttons ---> Start & Reset

# start
start_button = Button(text="Start", highlightthickness=0, command=start, font=(FONT_NAME, 10, "bold"))
start_button.grid(row=2, column=0)

# reset
reset_button = Button(text="Reset", highlightthickness=0, command=reset, font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2)


window.mainloop()