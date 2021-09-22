import turtle
import pandas

# pycharm likes to us .gif image files

screen = turtle.Screen()
screen.title("MARU U.S Map Game")

# Storing the image file path within 'image// make sure to use EXACT FILE NAME
image = "blank_states_img.gif"

# Loading the image shape into the screen
screen.addshape(image)

# Turning the turtle into the image
turtle.shape(image)

america = pandas.read_csv("50_states.csv")
states = america["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:

    guess = screen.textinput(title=f"Guess the state: {len(guessed_states)}/{50}",
                             prompt="What's another state's name ?").title()
    if guess == "Exit":
        missing_state = [state for state in states if state not in guessed_states]
        missing_state_dataframe = pandas.DataFrame(missing_state)
        missing_state_dataframe.to_csv("states_to_learn.csv")
        break

    # if guess == "Exit":
    #     missing_state = []
    #     for state in states:
    #         if state not in guessed_states:
    #             missing_state.append(state)
    #     missing_state_dataframe = pandas.DataFrame(missing_state)
    #     missing_state_dataframe.to_csv("states_to_learn.csv")
    #     break

    if guess in states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = america[america.state == guess]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(guess)  # using user value to put set states on map
        # t.write(states_data.state.item())  # getting the state name value from CSV




