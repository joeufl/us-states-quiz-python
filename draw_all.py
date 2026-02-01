import turtle
import pandas as pd

# --- Screen setup ---
screen = turtle.Screen()
screen.title("U.S. States Map — Draw All States")

IMAGE = "./images/blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# --- Load data ---
data = pd.read_csv("./data/50_states.csv")
# Expecting columns: state, x, y

# --- Writer turtle (single turtle for speed/cleanliness) ---
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

# Optional: adjust label style
FONT = ("Arial", 8, "normal")  # try 9 or 10 if you want larger

# --- Draw all states ---
for _, row in data.iterrows():
    state = str(row["state"])
    x = int(row["x"])
    y = int(row["y"])

    writer.goto(x, y)
    writer.write(state, align="center", font=FONT)

# Keep window open until click (or close button)
screen.exitonclick()