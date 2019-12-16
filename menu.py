print("Welcome to my Arcade!")
reply = input("Which game do you want to play?, TTT or Snake: ")
if reply == "TTT" :
    print("game on")
elif reply == "Snake" or reply == "snake":
    import turtle
    import time
    import random

    delay = 0.1

    score = 0
    high_score = 0

    background = turtle.Screen()
    background.title("THE NOKIA GAME")
    background.bgcolor("turquoise")
    background.setup(width=800, height=800) 
    background.tracer(0) 

    mouth = turtle.Turtle()
    mouth.speed(0)
    mouth.shape("square")
    mouth.color("pink")

    mouth.penup()
    mouth.goto(0,0)
    mouth.direction = "stop"

    chocolate = turtle.Turtle()
    chocolate.speed(0)
    chocolate.shape("circle")
    chocolate.color("yellow")

    chocolate.penup()
    chocolate.goto(0,100)

    segments = []

    result = turtle.Turtle()
    result.speed(0)
    result.shape("square")
    result.color("black")
    result.penup()
    result.hideturtle()
    result.goto(0,360)
    result.write("score: 0 high score: 0", align="center", font=("Georgia",24,"bold"))


    def go_up():
        if mouth.direction != "down":
            mouth.direction = "up"

    def go_left():
        if mouth.direction != "right":
            mouth.direction = "left"
        
    def go_down():
        if mouth.direction != "up":
            mouth.direction = "down"
        
    def go_right():
        if mouth.direction != "left":
            mouth.direction = "right"
        
    def move():
        if mouth.direction == "up":
            y = mouth.ycor()
            mouth.sety(y + 20)
        if mouth.direction == "down":
            y = mouth.ycor()
            mouth.sety(y - 20)
        if mouth.direction == "left":
            x = mouth.xcor()
            mouth.setx(x - 20)
        if mouth.direction == "right":
            x = mouth.xcor()
            mouth.setx(x + 20)


    background.listen()
    background.onkeypress(go_up,"w")
    background.onkeypress(go_down,"s")
    background.onkeypress(go_left,"a")
    background.onkeypress(go_right,"d")
    background.onkeypress(go_up,"W")
    background.onkeypress(go_down,"S")
    background.onkeypress(go_left,"A")
    background.onkeypress(go_right,"D")


    while True:
        background.update()

        if mouth.xcor()>390 or mouth.xcor()<-390 or mouth.ycor()>390 or mouth.ycor()<-390:
            time.sleep(1)
            mouth.goto(0,0)
            mouth.direction = "stop"

            
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            result.clear()
            result.write("Score: {} High Score: {}".format(score,high_score),align="center", font=("Georgia",24,"bold"))
            
        if mouth.distance(chocolate) < 20:
            x = random.randint(-390, 390)
            y = random.randint(-390, 390)
            chocolate.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("hot pink")
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001

            score += 10

            if score > high_score:
                high_score = score

            result.clear()
            result.write("Score: {} High Score: {}".format(score,high_score),align="center", font=("Georgia",24,"bold"))
        for index in range(len(segments)-1, 0,-1):
            x = segments[index -1].xcor()
            y = segments[index -1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = mouth.xcor()
            y = mouth.ycor()
            segments[0].goto(x, y)

        move()

        for segment in segments:
            if segment.distance(mouth) < 20:
                time.sleep(1)
                mouth.goto(0,0)
                mouth.direction = "stop"

                # Hide segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear  the segments
                segments.clear()

                score = 0

                # Reset the delay
                delay = 0.1
            
                # Update the score display
                result.clear()
                result.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Georgia", 24, "bold"))

        time.sleep(delay)

    background.mainloop()
