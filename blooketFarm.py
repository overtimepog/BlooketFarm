from __future__ import print_function
from calendar import c
import re
import os
import sys
import time
import random
from time import sleep
from itertools import groupby
from selenium import webdriver
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


if __name__ == "__main__":
    load_dotenv()

    Blooket_Username = os.getenv("username")
    Blooket_Password = os.getenv("password")
    Blooket = os.getenv("blooket")

    #Blooket_Username = "OvertimeDev"
    #Blooket_Password = "Dawgdawg2015"

    print(Blooket_Username)
    print(Blooket_Password)
    print(Blooket)
    i = 1

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element("xpath", xpath)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_css(css):
        try:
            driver.find_element(By.CSS_SELECTOR, css)
        except NoSuchElementException:
            return False
        return True
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    driver = uc.Chrome(desired_capabilities=d)
    try:
            driver.get("https://id.blooket.com/login")
            sleep(2)

            username = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/form/div[4]/input')
            username.click()
            username.send_keys(Blooket_Username)
            sleep(2)

            password = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/form/div[5]/input')
            password.click()
            password.send_keys(Blooket_Password)
            sleep(2)

            login = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/form/input')
            login.click()
            sleep(2)
            
            print("logged in")

            #create Lobby
            driver.get(Blooket)
            sleep(1)
            while i < 2:
                print("testing")
                if check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]') == True:
                    print("found")
                    #select Gold
                    sleep(2)
                    driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div/div[1]/img').click()
                    sleep(2)
                    while i < 2:
                        if check_exists_by_css("#hostGame") == True:
                            driver.find_element(By.CSS_SELECTOR, '#hostGame').click()
                            sleep(2)
                            print("Game Started")
                            break
                        elif check_exists_by_css("#hostGame") == False:
                            continue
                    sleep(2)
                    driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div[6]/div[2]/i').click()
                    sleep(1)
                    print("Turned off Instructions")
                    sleep(2)
                    #SetTime = 'document.querySelector("#app > div > div > div.styles__center___qMDUw-camelCase.styles__bigScreen___1OqJ1-camelCase > div.styles__mainContainer___1doVE-camelCase > div.styles__amountContainer___3IhWu-camelCase > input").value = ' + BlooketTime
                    #sleep(2)
                    #driver.execute_script(SetTime)
                    
                    #time doesnt seem to be changing, idk why, it seems to work beyond 7 but not before 7 
                    
                    #print("Time Set to " + BlooketTime + " minutes")
                    #sleep(2)
                    
                    while i < 2:
                        if check_exists_by_css("#hostNow") == True:
                            driver.find_element(By.CSS_SELECTOR, '#hostNow').click()
                            sleep(2)
                            print("Game Started")
                            break
                        elif check_exists_by_css("#hostNow") == False:
                            continue
                  
                    while i < 2:
                        if check_exists_by_xpath('//*[@id="idNum"]') == True:
                            code = driver.find_element('xpath', '//*[@id="idNum"]').text
                            print("Lobby Code: " + code)
                            break
                        elif check_exists_by_xpath('//*[@id="idNum"]') == False:
                            continue
                    break
                elif check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]') == False:
                    print("not found")
                    continue
                
            print('Lobby Online :)')
            print('\n')

        #join Lobby
                
            #create Farmer
            driver.execute_script("window.open('');")
            sleep(5)
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://play.blooket.com/play")
            #print("Opened Bot " + str(bot) + "'s page")
            
            while i < 2: #code loop
                if check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div[1]/input") == True:
                    codeEnter = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[1]/input')
                    codeEnter.send_keys(code)
                    sleep(1)
                    codeEnter.send_keys(Keys.ENTER)
                    sleep(2)
                    break
                    
                elif check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div[1]/input") == False:
                    continue
                
                
            while i < 2: #name loop
                if check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/input") == True:
                    nameEnter = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
                    name = "Farmer"
                    nameEnter.send_keys(name)
                    sleep(1)
                    nameEnter.send_keys(Keys.ENTER)
                    sleep(2)
                    break
                
                elif check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/input") == False:
                    continue
                
            
            print("Farmer Joined Lobby " + code)
            print("\n")
            
            
        #start Game
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            while i < 2:
                if check_exists_by_xpath("//*[@id='startGame']") == True:
                    sleep(2)
                    driver.find_element('xpath', '//*[@id="startGame"]').click()
                    sleep(2)
                    break
                elif check_exists_by_xpath("//*[@id='startGame']") == False:
                    continue
            print('Game Started')
            print('\n')
            
            
        #play Game
            sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            #allRight = 'let hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner; for (let i = 0; i < hack.stateNode.questions.length; i++) { hack.stateNode.questions[i].correctAnswers = hack.stateNode.questions[i].answers; hack.stateNode.forceUpdate(); }'
            #driver.execute_script(allRight)
            #print('AllRight.js Injected')
            while i < 2:
                driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                print('hack Injected')
                stage = driver.execute_script("return hack.stateNode.state.stage")
                answer = driver.execute_script("return hack.stateNode.state.question.correctAnswers.toString()")
                choiceLength = driver.execute_script("return hack.stateNode.state.choices.length")
                
                stringStage = str(stage)
                print("answer: " + answer)
                print("stage: "+ stringStage)
 
                if (choiceLength == 0) == True:
                    print("No Choices")
                    pass
                
            
                if (stringStage == "question") == True:
                    sleep(1)
                    answer0 = driver.find_element("xpath", '//*[@id="answer0"]/div/div/div/div').text
                    answer1 = driver.find_element("xpath", '//*[@id="answer1"]/div/div/div/div').text
                    answer2 = driver.find_element("xpath", '//*[@id="answer2"]/div/div/div/div').text
                    answer3 = driver.find_element("xpath", '//*[@id="answer3"]/div/div/div/div').text
                    
                    if answer == answer0:
                        driver.find_element("xpath", '//*[@id="answer0"]/div/div/div/div').click()
                        sleep(1)
                        continue
                    else:
                        pass
                    
                    if answer == answer1:
                        driver.find_element("xpath", '//*[@id="answer1"]/div/div/div/div').click()
                        sleep(1)
                        continue
                    else:
                        pass
                    
                    if answer == answer2:
                        driver.find_element("xpath", '//*[@id="answer2"]/div/div/div/div').click()
                        sleep(1)
                        continue
                    else:
                        pass
                    
                    if answer == answer3:
                        driver.find_element("xpath", '//*[@id="answer3"]/div/div/div/div').click()
                        sleep(1)
                        continue
                    else:
                        pass
    
                sleep(2)
                
                

                    
                if (stringStage == "prize") == True:
                    driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                    print('hack 2 Injected')
                    choiceType1 = driver.execute_script("return hack.stateNode.state.choices[0].type")
                    choiceType2 = driver.execute_script("return hack.stateNode.state.choices[1].type")
                    choiceType3 = driver.execute_script("return hack.stateNode.state.choices[2].type")
                    print("choice 1: " + choiceType1)
                    print("choice 2: " + choiceType2)
                    print("choice 3: " + choiceType3)
                    
                        
                        
                    if (choiceType1 == "divide") == True:
                        pass
                    if (choiceType1 == "take") == True:
                        pass  
                    if (choiceType1 == "swap") == True:
                        pass                       
                    if (choiceType1 == "multiply") == True:
                        driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                        continue
                    else:
                        pass                          
                    if (choiceType1 == "gold") == True:
                        driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                        continue
                    else:
                        pass
                        
                    
                    if (choiceType2 == "divide") == True:
                        pass
                    if (choiceType2 == "take") == True:
                        pass  
                    if (choiceType2 == "swap") == True:
                        pass                       
                    if (choiceType2 == "multiply") == True:
                        driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()   
                        continue                        
                    else:
                        pass
                    if (choiceType2 == "gold") == True:
                        driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                        continue
                    else:
                        pass
                        
                    
                    if (choiceType3 == "divide") == True:
                        pass
                    if (choiceType3 == "take") == True:
                        pass  
                    if (choiceType3 == "swap") == True:
                        pass                       
                    if (choiceType3 == "multiply") == True:
                        driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                        continue
                    else:
                        pass
                    if (choiceType3 == "gold") == True:
                        driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                        sleep(1)
                        driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                        continue
                    else:
                        pass    
                pass
                
                if (stringStage == "feedback") == True:
                    driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                    driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                    continue
                    
  
            
    except Exception as e: print(e)   