from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    
# Variables that user has to input
try:
    open('people-also-ask.txt', 'w').close()
except: 
    print("Create a file in the same directory as 'people-also-ask.txt'")

query = input("Input your keyword: ")
clicks = int(5)
lang = 'en'
file_open = ''
try:
    file_open = open('people-also-ask.txt', 'a')
    file_open.write(f'Keyword: {query}\n')
except:
    print("Create a file in the same directory as 'people-also-ask.txt'")

def search(query, clicks):
    
    #headless option so it doesnt open chrome everytime we run it
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False 

    driver = webdriver.Chrome(options=chrome_options,executable_path='chromedriver.exe')  # Optional argument, if not specified will search path.
   
    driver.get("https://www.google.com?hl=en")

    print('The keyword you selected is:', query)
    print(' Number of clicks we will do is:',clicks)

    driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys(query+Keys.RETURN)
    print(query)
    clickingKW(clicks,driver)

"""Function that clicks N Questions.
Parameters: - clicks: number of clicks we will use on the questions
            - driver: Driver that we are using"""

def clickingKW(clicks,driver): 
    for i in range(clicks):
        print('Clicking question #',i+1)
        paa = driver.find_elements_by_xpath("//*[@jsname='K8Pnod']")
        try:
            paa[i].click()
            print('clicked')
            time.sleep( 2 )
        except:
            continue
    

    questionsofpaa = driver.find_elements_by_xpath("//*[@jsname='jIA8B']/span")
    try:
        for j in questionsofpaa:
            file_open.write(j.text)
            file_open.write('\n')

    except: 
        print("There are no questions in the PEOPLE ALSO ASK section")


search(query,clicks)