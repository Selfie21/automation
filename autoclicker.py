import pyautogui
import time
import random

#Set Positions/Colours
color_again = [240, 185, 11]
color_green = [10, 181, 107]
color_red = [164, 70, 88]

base_again = [1420, 455]
base_cnt = [1205, 301]
base_long = [1140, 475]
base_short = [1490, 475]
base_result = [1544, 796]


def short_click(positions, randomizer):
	pyautogui.click(positions[0]+randomizer, positions[1]-randomizer)

def click_routine(randomizer_time, randomizer_position):
	randomizer_way = random.randint(0,1)
	time.sleep(randomizer_time)
	short_click(base_again, randomizer_position)
	time.sleep(randomizer_time + 5)
	short_click(base_cnt, randomizer_position)
	time.sleep(randomizer_time)
	
	if randomizer_way:
		short_click(base_short, randomizer_position)
	else:
		short_click(base_long, randomizer_position)

def check_matching_array(arr1, arr2):
	return (arr1[0] == arr2[0]) and (arr1[1] == arr2[1]) and (arr1[2] == arr2[2])

def get_colour(coords):
	return pyautogui.pixel(coords[0],coords[1])


while True:
	randomizer_position = random.randint(0,10)
	randomizer_time = random.randint(0,15)
	randomizer_short = random.randint(1, 3)
	current_color = get_colour(base_again)
	
	if check_matching_array(current_color, color_again):
		click_routine(randomizer_short, randomizer_position)
	
	time.sleep(10 + randomizer_time)


