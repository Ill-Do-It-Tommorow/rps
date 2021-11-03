let player_a_score = 0
let player_b_score = 0
let selection = 0
input.onButtonPressed(Button.A, function () {
    player_a_score += 1
    if (player_a_score == 7) {
        basic.showString("Player A wins!")
        player_a_score = 0
        player_b_score = 0
    }
})
input.onButtonPressed(Button.B, function () {
    player_b_score += 1
    if (player_b_score == 7) {
        basic.showString("Player B wins!")
        player_a_score = 0
        player_b_score = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    selection = randint(1, 3)
    if (selection == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (selection == 2) {
        basic.showIcon(IconNames.Square)
    } else if (selection == 3) {
        basic.showIcon(IconNames.Scissors)
    }
})
