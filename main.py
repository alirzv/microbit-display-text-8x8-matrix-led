def on_button_pressed_a():
    max7219_matrix.scroll_text("Welcome to Naba's home! We are having party today in Z block.",
        75,
        500)
    max7219_matrix.fill_all()
    basic.pause(500)
    max7219_matrix.clear_all()
    max7219_matrix.fill_all()
    basic.pause(500)
    max7219_matrix.clear_all()
    max7219_matrix.fill_all()
    basic.pause(500)
    max7219_matrix.clear_all()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global temp
    temp = input.temperature()
    max7219_matrix.display_text(convert_to_text(temp), 0, True)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    max7219_matrix.scroll_text("Party!", 25, 500)
    for i in range(50):
        max7219_matrix.clear_all()

    for i in range(50):
        max7219_matrix.clear_all()
        max7219_matrix.randomize_all()
        basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

temp = 0
max7219_matrix.setup(4,
    DigitalPin.P16,
    DigitalPin.P15,
    DigitalPin.P14,
    DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.CLOCKWISE, False)

def on_forever():
    pass
basic.forever(on_forever)

max7219_matrix.get_empty_matrix()
max7219_matrix.get_value_from_matrix([], 0, 0)