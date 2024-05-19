from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import requests
import json
import re
import urllib

driver = webdriver.Chrome()

driver.get("https://rp5.ru/Weather_archive_in_Usti_nad_Labem")

def get_synop(wmo_id: str, driver: webdriver.Chrome, from_date: str, to_date: str):
    wmo_id_input_ele = driver.find_element(By.ID, 'wmo_id')
    wmo_id_input_ele.clear()
    wmo_id_input_ele.send_keys(wmo_id)
    time.sleep(3)
    station_link = driver.find_elements(By.CSS_SELECTOR, '.ac_even')
    if not station_link: return
    else: station_link = station_link[0]
    station_link.click()
    time.sleep(.5)
    driver.find_element(By.ID, 'tabSynopDLoad').click()
    from_date_ele = driver.find_element(By.ID, 'calender_dload')
    from_date_ele.clear()
    from_date_ele.send_keys(from_date)
    to_date_ele = driver.find_element(By.ID, 'calender_dload2')
    to_date_ele.clear()
    to_date_ele.send_keys(to_date)
    driver.find_element(By.ID, 'format2').find_element(By.XPATH, '..').click() # csv format
    driver.find_element(By.ID, 'coding2').find_element(By.XPATH, '..').click() # utf-8 enc
    driver.find_element(By.CSS_SELECTOR, '.download div.archButton').click() # select to file GZ archive
    download_button_ele = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="f_result"]/a')))
    download_button_ele.click()

if __name__ == '__main__':
    get_synop('11450', driver, '1.1.2023', '31.12.2023')
    input()