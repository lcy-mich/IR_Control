import serial
from pynput import mouse, keyboard

SPEED = 20

baudrate = 115200
portname = "COM7"

ser = serial.Serial(portname, baudrate)
ms = mouse.Controller()
kb = keyboard.Controller()

while True:
    line = ser.readline().strip()
    if len(line) and line != b'ERR':
        match line:
            case b'1': #left up
                ms.move(-SPEED//1.41, -SPEED//1.41)
            case b'2': #up
                ms.move(0, -SPEED)
            case b'3': #right up
                ms.move(SPEED//1.41, -SPEED//1.41)
            case b'4': #left
                ms.move(-SPEED, 0)
            case b'5': #press
                kb.press(" ")
            case b'6': #right
                ms.move(SPEED, 0)       
            case b'7': #left down
                ms.move(-SPEED, SPEED)
            case b'8': #down
                ms.move(0, SPEED)
            case b'9': # down right
                ms.move(SPEED, SPEED)

            case b'100+':
                ms.click(mouse.Button.middle)
            case b'200+':
                ms.click(mouse.Button.right)
            case b'0':
                ms.click(mouse.Button.left)

            case b'VOL-':
                kb.press(keyboard.Key.media_volume_down)
            case b'VOL+':
                kb.press(keyboard.Key.media_volume_up)
            case b'EQ':
                kb.press(keyboard.Key.media_volume_mute)

            case b'PREV':
                kb.press(keyboard.Key.media_previous)
            case b'NEXT':
                kb.press(keyboard.Key.media_next)
            case b'PLAY/PAUSE':
                kb.press(keyboard.Key.media_play_pause)
            
            case b'CH-':
                kb.press(keyboard.Key.esc)
            case b'CH':
                kb.press(keyboard.Key.scroll_lock)
            case b'CH+':
                kb.press(keyboard.Key.tab)
            case _:
                continue