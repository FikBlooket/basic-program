def on_forever():
    basic.show_string("Hello!")
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_string("67")
    basic.show_leds("""
        . . . # .
        . . # . .
        . # # # .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        # # # # #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . #
        . # # # .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        . # # # .
        # . . . #
        . # # # .
        . . # . .
        . # . . .
        """)
    basic.show_string("67")
    basic.show_string("MR.Beast")
    basic.show_string("GIMME some MONEY!!!!")
    basic.show_string("FIKUNOLAMI")
basic.forever(on_forever)
