print("Welcome to my Arcade!")
reply = 0
print("Games available\n\t Game 1 - TTT\n\t Game 2 - Snake")

while True:
    try:
        while (reply < 1) or (reply > 2):
            reply = int(input("Which game do you want to play? Game 1 or Game 2: "))
        break
    except ValueError:
        print("Please enter a valid input")

if reply == 1 :
    board = ['-','-', '-',
            '-', '-', '-',
            '-', '-', '-',]

    game_is_still_going = True

    winner = None 

    current_player = "X"

    def play_game() :

        display_board()

        while game_is_still_going :

            handle_turn(current_player)

            check_if_game_over()

            flip_player()
        if winner == "X" or winner == "0":
            print(winner + "  WON!")
        elif winner == None:
            print("It's a tie :(((((")

    def display_board():
        print("\n")
        print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
        print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
        print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
        print("\n")

    def handle_turn(player):

        print(player + "'s turn.")
        position = input("Choose a position from 1-9: ")

        valid = False
        while not valid :

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")


            position = int(position) - 1

            if board[position] == '-':
                valid = True
            else:
                print("You cant do that. Retry")

            board[position] = player
            display_board() 

    def check_if_game_over():
        check_for_winner()
        check_if_tie()

    def check_for_winner():
        global winner
        row_winner = check_rows()
        column_winner = check_columns()
        diagonal_winner = check_diagonals()
        if row_winner:
            winner = row_winner
        elif column_winner:
            winner = column_winner
        elif diagonal_winner:
            winner = diagonal_winner
        else:
            winner = None

    def check_rows():
        global game_is_still_going
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        if row_1 or row_2 or row_3:
            game_is_still_going = False
        
        if row_1:
            return board[0] 
        elif row_2:
            return board[3] 
        elif row_3:
            return board[6] 
        else:
            return None

    def check_columns():
        
        global game_is_still_going
        
        column_1 = board[0] == board[3] == board[6] != "-"
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"
    
        if column_1 or column_2 or column_3:
            game_is_still_going = False
        
        if column_1:
            return board[0] 
        elif column_2:
            return board[1] 
        elif column_3:
            return board[2] 

        else:
            return None

    def check_diagonals():
        
        global game_is_still_going
        
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"
        
        if diagonal_1 or diagonal_2:
            game_is_still_going = False
        
        if diagonal_1:
            return board[0] 
        elif diagonal_2:
            return board[2]
        
        else:
            return None

    def check_if_tie():
        global game_is_still_going
        if "-" not in board :
            game_is_still_going = False
        else:
            return False

    def flip_player():
        
        global current_player

        if current_player == "X":
            current_player = '0'

        elif current_player == "0":
            current_player = 'X'


    play_game()
        
elif reply == 2:
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
    background.bgpic("final1.gif")

    turtle.register_shape("choc1.gif")
    turtle.register_shape("mouth.gif")

    mouth = turtle.Turtle()
    mouth.speed(0)
    mouth.shape("mouth.gif")
    mouth.color("pink")

    mouth.penup()
    mouth.goto(0,0)
    mouth.direction = "stop"

    chocolate = turtle.Turtle()
    chocolate.speed(0)
    chocolate.shape("choc1.gif")
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
            new_segment.shape("circle")
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
  
