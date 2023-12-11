from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import itertools
import csv

geckodriver_path = 'E:/geckodriver.exe'#enter the path for your driver

service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(service=service)

import time







driver.get('https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D')
try:
    element=WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        ('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
    element.send_keys('gauravdev818@gmail.com')
except WebDriverException:
    print("Tweets did not appear!, Try setting headless=False to see what is happening")
    
driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
# driver.implicitly_wait(10)
# driver.find_element('xpath','/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys('hb_gaurav')
# driver.find_element('xpath','/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
driver.implicitly_wait(10)
driver.find_element('xpath','/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('Gaurav@123');
driver.find_element('xpath','/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
driver.implicitly_wait(10)
element=driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
element.send_keys('#Palestine')
element.send_keys(Keys.ENTER)
driver.implicitly_wait(10)



driver.find_element('xpath','//div[@data-testid="tweetText"]').click()
driver.implicitly_wait(10)



time.sleep(5)
    
tweets = []
result = False
old_height = driver.execute_script("return document.body.scrollHeight")

#set initial all_tweets to start loop
all_tweets = driver.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

while result == False:

    for item in all_tweets[1:]: # skip tweet already scrapped
        try:
           
            ad_indicator = item.find_elements(By.XPATH, './/span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" and contains(text(), "Ad")]')
            if ad_indicator:
                print("Skipping ad tweet")
                continue 
        except StaleElementReferenceException:
            print("Stale element exception, refreshing elements.")
            all_tweets = driver.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')
            continue

        print('--- text ---')
        try:
            text = item.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
        except:
            text = '[empty]'
        print(text)

        
    
        #Append new tweets replies to tweet array
        tweets.append([ text])
    
    #scroll down the page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(2)
    
    try:
        try:
            button = driver.find_element_by_css_selector("div.css-901oao.r-1cvl2hr.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0")
        except:
            button = driver.find_element_by_css_selector("div.css-1dbjc4n.r-1ndi9ce") #there are two kinds of buttons
        
        ActionChains(driver).move_to_element(button).click(button).perform()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
    except:
        pass

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == old_height:
        result = True
    old_height = new_height

    #update all_tweets to keep loop
    all_tweets = driver.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

# tweets = tweets.sort()





csv_file_name = 'tweets.csv'

with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(tweets)

print(f'CSV file "{csv_file_name}" has been created.')



