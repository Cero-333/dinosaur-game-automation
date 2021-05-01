from selenium import webdriver
from PIL import Image, ImageGrab
import pyautogui
import time
import os

# whole canvas position
top, left, width, height = 400, 0, 1890, 700

# bird area
y_search_bird = 275
# cactus area
y_search_cactus = 100
x_start, x_end = 650, 690
# dino acceleration point
acc = 0

exe_path = os.environ.get("EXE_PATH")
driver = webdriver.Chrome(exe_path)
driver.get("https://elgoog.im/t-rex/")

time.sleep(2)
# starting the game
pyautogui.press("up")
time.sleep(2)

round = 0


def check_obstacle(image: Image):
    """
    Checks whether there is a cactus or bird in sight by comparing the RGB values of pixels.
    """
    total = 0
    data = image.load()
    for x in range(x_start + acc, x_end + acc):
        if data[x, y_search_cactus] == (83, 83, 83):
            total += 1
        elif data[x, y_search_bird] == (83, 83, 83):
            total += 1

    if total > 0:
        return True
    return False


while True:
    inst_img = ImageGrab.grab(bbox=(left, top, width, height)).convert("RGB")
    if check_obstacle(inst_img):
        pyautogui.press("up")

    # adjusting the bird/cactus area according to dinosaur's speed.
    round += 1
    if round % 10 == 0:
        acc += 4

# somebody has to stop this manually after the game ends xD
