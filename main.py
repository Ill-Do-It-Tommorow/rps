player_a_score = 0
player_b_score = 0
selection = 0

def on_button_pressed_a():
    global player_a_score, player_b_score
    player_a_score += 1
    if player_a_score == 7:
        basic.show_string("Player A wins!")
        player_a_score = 0
        player_b_score = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global player_b_score, player_a_score
    player_b_score += 1
    if player_b_score:
        basic.show_string("Player B wins!")
        player_a_score = 0
        player_b_score = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global selection
    selection = randint(1, 3)
    if selection == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif selection == 2:
        basic.show_icon(IconNames.SQUARE)
    elif selection == 3:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
