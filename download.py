import time
import urllib.request
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def perform_search(keyword, searchbar):
    # Remove content from Search Bar
    ActionChains(driver) \
        .move_to_element(searchbar) \
        .click() \
        .key_down(Keys.CONTROL)\
        .send_keys("a")\
        .key_up(Keys.CONTROL)\
        .send_keys(Keys.BACK_SPACE)\
        .perform()

    # Input Keyword
    ActionChains(driver) \
        .send_keys(keyword)\
        .send_keys(Keys.ENTER)\
        .perform()

def download_foto():
    first_pic = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.isv-r:nth-child(2) > a:nth-child(2) > div:nth-child(1) > img:nth-child(1)")))
    return first_pic.get_attribute('src')

driver = webdriver.Firefox()
driver.get('https://www.google.de/imghp?hl=de')
accept_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
accept_button.click()
search_field_beginning = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
perform_search("start", search_field_beginning)

wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
list = [
"Michelada",
"Atole",
"Té de Guayaba",
"Submarino Bebida Cola",
"Raspado de Piña",
"Balazo de Camarón",
"Elote",
"Tamal",
"Sopes",
"Quesadilla de Queso y Huitlacoche",
"Chapulínes",
"Sopa Pozole Rojo",
"Enchiladas de Mole",
"Gorditas",
"Churros con Philadelphia",
"Sopa Azteca",
"Cemita Poblana",
"Chilepotle Navideño",
"Papalo",
"Sopa de Papa",
"Chilaquiles",
"Huitlacoche",
"Totopos",
"Germen de Alfalfa",
"Chicharrón",
"Leche con Arroz",
"Tlayoyos",
"Albóndigas",
"Molotes",
"Tacos",
"Picadita Veracruzana",
"Pambazo Veracruzana",
"Nachos preparados con Esquite y Camarón",
"Chevere (Empanadas)",
"Alambres de Pollo",
"Mollete con Carne de Pastor",
"Pozolo con Guerrerense"]

for word in list:
    search_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="REsRA"]')))
    perform_search(word, search_field)
    time.sleep(0.5)
    src_pic = download_foto()
    time.sleep(0.5)
    #print(src_pic)
    #urllib.request.urlretrieve(src_pic, word + ".jpg")


