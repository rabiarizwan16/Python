import turtle
import pandas
screen=turtle.Screen()
screen.title("Indian States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)
data =pandas.read_csv("states_data.csv")
all_state=data.state.to_list()
print(all_state)
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 the State Correct",
                                  prompt="What's another name?").title()
    if answer_state=="Exit":
        missing_state = [state for state in all_state if state not in guessed_state]
        new_data=pandas.DataFrame(missing_state)
        new_data.to.csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

