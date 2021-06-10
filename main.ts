input.onButtonPressed(Button.A, function on_button_pressed_a() {
    max7219_matrix.scrollText("Welcome to Naba's home! We are having party today in Z block.", 75, 500)
    max7219_matrix.fillAll()
    basic.pause(500)
    max7219_matrix.clearAll()
    max7219_matrix.fillAll()
    basic.pause(500)
    max7219_matrix.clearAll()
    max7219_matrix.fillAll()
    basic.pause(500)
    max7219_matrix.clearAll()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    temp = input.temperature()
    max7219_matrix.displayText(convertToText(temp), 0, true)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let i: number;
    max7219_matrix.scrollText("Party!", 25, 500)
    for (i = 0; i < 50; i++) {
        max7219_matrix.clearAll()
    }
    for (i = 0; i < 50; i++) {
        max7219_matrix.clearAll()
        max7219_matrix.randomizeAll()
        basic.pause(200)
    }
})
let temp = 0
max7219_matrix.setup(4, DigitalPin.P16, DigitalPin.P15, DigitalPin.P14, DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.clockwise, false)
basic.forever(function on_forever() {
    
})
max7219_matrix.getEmptyMatrix()
max7219_matrix.getValueFromMatrix([], 0, 0)
