import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writing = turtle.Turtle()
writing.penup()
writing.hideturtle()


data = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = data.state.to_list()


while len(guessed_states) != 50:
    guessed_states_num = len(guessed_states)
    answer_state = (turtle.textinput(title=f"States Correct ({guessed_states_num}/50)",
                                     prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        output = pandas.DataFrame(missing_states)
        output.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        validated_data = data[data.state == answer_state]
        xcor = validated_data.x.item()
        ycor = validated_data.y.item()
        writing.setposition(xcor, ycor)
        writing.write(answer_state)
        guessed_states.append(answer_state)



