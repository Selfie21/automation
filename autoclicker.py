import pyautogui
import signal
import time
import random

#Set Positions/Colours
color_grey = [43, 47, 54]
color_yellow = [240, 185, 11]
color_yellow_two = [248, 209, 47]
base_again = [1385, 445]
base_end = [1420, 445]
base_cnt = [1205, 301]
base_long = [1140, 475]
base_short = [1490, 475]
base_result = [1544, 797]


#Click Stuff
def click_startup_routine(randomizer_time):
	randomizer_way = random.randint(0,1)
	time.sleep(randomizer_time)
	short_click(base_again)
	time.sleep(randomizer_time + 5)
	short_click(base_cnt)
	time.sleep(randomizer_time)
	
	if randomizer_way:
		short_click(base_short)
	else:
		short_click(base_long)
	time.sleep(13)

def short_click(positions):
	pyautogui.click(positions[0], positions[1])


#Colour Stuff
def check_matching_array(arr1, arr2):
	return (arr1[0] == arr2[0]) and (arr1[1] == arr2[1]) and (arr1[2] == arr2[2])

def get_colour(coords):
	return pyautogui.pixel(coords[0],coords[1])

def check_for_colour_change(coords):
	while not ((get_colour(coords)[1] > 100) and (get_colour(coords)[1] < 200)):
		time.sleep(0.01)
	return True
	

#Timeout Handler
def handler(signum, frame):
	raise Exception("Timeout")


while True:
	randomizer_time = random.randint(0,15)
	current_color = get_colour(base_again)
	print("Calling Startup Routine;")
	if check_matching_array(current_color, color_yellow) or check_matching_array(current_color, color_yellow_two):
		randomizer_short = random.randint(1, 3)
		click_startup_routine(randomizer_short)
	
	
	#ending Battle
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(300)

	try:
		if check_for_colour_change(base_result):
			print("I found green clicking now! Click routine can continue;")
			short_click(base_end)
	except Exception: 
		print("Timeout Occurred;")
	signal.alarm(0)
	
	time.sleep(10 + randomizer_time)
