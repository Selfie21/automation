import pyautogui
import random
import time

location_buy = [875, 855]
location_buy_2 = [991, 384]
location_zu_kasse = [1474, 812]
colour_buy = [255, 120, 0]
location_plus = [1097, 766]


# Colour Stuff
def check_for_colour_change(coords, colour):
    for i in range(0, 50):
        if check_matching_array(colour, get_colour(coords)):
            return True
        time.sleep(0.01)
    return False


def check_matching_array(arr1, arr2):
    return (arr1[0] == arr2[0]) and (arr1[1] == arr2[1]) and (arr1[2] == arr2[2])


def get_colour(coords):
    return pyautogui.pixel(coords[0], coords[1])


# Click Stuff
def buying_routine():
    short_click(location_plus)
    time.sleep(0.2)
    short_click(location_plus)
    time.sleep(0.2)
    short_click(location_buy)
    time.sleep(1)
    short_click(location_buy_2)
    time.sleep(1)
    short_click(location_zu_kasse)


def short_click(coords):
    pyautogui.click(coords[0], coords[1])


time.sleep(1)

while True:
    pyautogui.press('f5')
    time.sleep(0.5)
    if check_for_colour_change(location_buy, colour_buy):
        buying_routine()
        time.sleep(600)

    randomizer_time = random.randint(4, 8)
    time.sleep(randomizer_time)
