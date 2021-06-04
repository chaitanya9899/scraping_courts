import time
import body as body
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,TimeoutException,JavascriptException,StaleElementReferenceException
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# install and download to google 
chrome_options = webdriver.ChromeOptions()
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.maximize_window()
#web site url 
driver.get("https://oresundskraft.se/energiportalen/logga-in/")




#login details
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/input").send_keys("teknik.malmo@nyfosa.se")

driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/div[2]/div[2]/input").send_keys("Kaffe2021")

driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/div[3]/div[1]/button").click()
time.sleep(10)
driver.execute_script(('window.scrollTo(0,50);'))
startlink=1
time.sleep(5)

# login into website
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/ul/li[1]').click()
time.sleep(5)
x=100
for i in range(0,30):
    
    items=driver.find_elements_by_class_name('invoice-list-item')
    time.sleep(5)
    print(len(items))
   
    print("start")
    print(startlink)
        
    print("End")
    for i in range(startlink,len(items)):
        Betald=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/div[2]/ul/li['+str(i)+']/div/div/div[5]')
        print(Betald.text)
        print(i)
        x+=80
        driver.execute_script(('window.scrollTo(0, {0});'.format(x)))
        if Betald.text =='Betald':
            
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/div[2]/ul/li["+str(i)+"]/div/div/div[5]").click()
            pdf_link=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/div[2]/ul/li[1]/div/div/div[7]/div[6]/div/span/a")
            print(pdf_link)
            driver.execute_script("arguments[0].setAttribute('download','')",pdf_link)
            time.sleep(5)
            pdf_link.click()
    ## append value of list
    startlink=len(items)
    ##click for next button
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/div[2]/div[2]/div/div/span").click()
    except:
        print("Completed Done")
        
        
        

