"""
This script is used to play the game Piano Tiles 2 automatically.
you may need to change the gameCoords variable to match the coordinates of the game area on your screen.
and you may need to change the click_block function to match the color of the tiles in your game.
"""
import numpy as np
import keyboard
import time
import cv2
from PIL import ImageGrab

# Coordinates of the piano tiles game area
gameCoords = (393, 72, 932, 948)

# Variables
score = 0
previousLane = -1
previousY = [0, 0, 0, 0]


def click_block(screen):
    global gameCoords, score, previousLane, previousY
    for y_ in range(5, len(screen) - 5, 5):
        for i in range(4):
            if previousLane == i and y_ >= previousY[i] - 10:
                continue
            w = gameCoords[2] - gameCoords[0]
            x = int(i * w / 4 + w / 8)
            y = len(screen) - y_
            if screen[y, x] < 40:
                if i == 0:
                    keyboard.press_and_release('a')
                    print("a")
                elif i == 1:
                    keyboard.press_and_release('s')
                    print("s")
                elif i == 2:
                    keyboard.press_and_release('d')
                    print("d")
                elif i == 3:
                    keyboard.press_and_release('f')
                    print("f")
                previousLane = i
                previousY[i] = y_
                return


while True:
    screen = np.array(ImageGrab.grab(bbox=gameCoords))
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    click_block(screen_gray)
    time.sleep(0.1)

    # Press 'q' to quit

    if keyboard.is_pressed('q'):
        break
