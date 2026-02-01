import turtle
import pandas

#Screen setup
screen = turtle.Screen()
screen.title("U.S. States Quiz")
IMAGE = "./images/blank_states_img.gif"
screen.addshape(IMAGE) #Convert to a shape type
turtle.shape(IMAGE) #Use of the images as shape type

#Mausklick-Koordinaten erhalten
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

#Get Data
guessed_states = []
data = pandas.read_csv("./data/50_states.csv")
state_list = data["state"].to_list()

current_text = ""

input_writer = turtle.Turtle()
input_writer.hideturtle()
input_writer.penup()
input_writer.goto(-200, 260)  # top-left-ish above map

def draw_input():
    input_writer.clear()
    input_writer.write(
        f"{len(guessed_states)}/50  Guess a state: {current_text}",
        font=("Arial", 16, "normal")
    )

def submit_answer():
    global current_text
    answer_state = current_text.title()
    current_text = ""
    draw_input()

    if answer_state == "Exit":
        missing_states = [s for s in state_list if s not in guessed_states]
        pandas.DataFrame(missing_states,columns=["state"]).to_csv(
            "./data/states_to_learn.csv",
            index=False
        )
        screen.bye()
        return

    if answer_state in state_list and answer_state not in guessed_states:
        state_row = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)
    draw_input()

def add_char(char):
    global current_text
    current_text += char
    draw_input()

def backspace():
    global current_text
    current_text = current_text[:-1]
    draw_input()

screen.listen()

for letter in "abcdefghijklmnopqrstuvwxyz":
    screen.onkey(lambda l=letter: add_char(l), letter)

screen.onkey(backspace, "BackSpace")
screen.onkey(submit_answer, "Return")

draw_input()
turtle.mainloop()