#!/usr/bin/python3

import sys
import time

import telegram
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

in_stock = False
telegram_token = "1787042062:AAFkJpKMu33FzHV5_VeV0B-7IBN4_50SHTU"
telegram_chat_ids = ["444357534"]

while True:
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789"
    driver.get(url)
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button"))).click()
        in_stock = True
    except TimeoutException:
        print("Not in stock wait for 1 Seconds!")

    if in_stock:
        bot = telegram.Bot(token=telegram_token)
        for chat_id in telegram_chat_ids:
            try:
                bot.send_message(chat_id=chat_id, text="GPU AVAILABLE!!!")
            except Exception as e:
                print(f"Fehler beim Versenden der Telegram-Nachricht an {chat_id}: {e}")
        time.sleep(5)
        driver.find_element_by_xpath(
            "/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a").click()
        time.sleep(4)
        try:
            driver.find_element_by_xpath(
            "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[1]/form/ul/li[2]/div[1]/div/div/div/input").click()
        except Exception:
            driver.find_element_by_xpath(
            "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button").click()
        time.sleep(5)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button").click()
        sys.exit(0)

    time.sleep(1)
