number = 0

def on_button_pressed_a():
    basic.show_number(randint(1, 6))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global number
    number = randint(1, 6)
    if number == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    else:
        if number == 2:
            basic.show_leds("""
                . . . . .
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                """)
        else:
            if number == 3:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . # # # .
                    . . . . .
                    . . . . .
                    """)
            else:
                if number == 4:
                    basic.show_leds("""
                        . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
                        """)
                else:
                    if number == 5:
                        basic.show_leds("""
                            . . . . .
                            . # . # .
                            . . # . .
                            . # . # .
                            . . . . .
                            """)
                    else:
                        if number == 6:
                            basic.show_leds("""
                                . . . . .
                                . # . # .
                                . # . # .
                                . # . # .
                                . . . . .
                                """)
                        else:
                            basic.show_string("This number is invalid.")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
