from __future__ import print_function
from pickle import TRUE
import re
import os
import sys
import time
import random
import threading
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
    BlooketTime = os.getenv("time")
    Blooket = os.getenv("blooket")

    #Blooket_Username = "OvertimeDev"
    #Blooket_Password = "Dawgdawg2015"

    print("Username " + Blooket_Username)
    print("Password " + Blooket_Password)
    print("Seconds: " + BlooketTime)
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
    
    #SECTION - End Game Function
    def endGame():
        #switch tabs, and hit end button
                driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                stage = driver.execute_script("return hack.stateNode.state.stage")
                
                sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                print("Switched to Host Tab")
                sleep(1)
                
                driver.find_element("xpath", '//*[@id="app"]/div/div/div[1]/div[3]/i').click()
                print("Clicked End Game")
                
                driver.switch_to.window(driver.window_handles[1])
                print("\n")
                sleep(4)
                #xp multiplier button
                while i < 2:
                    if check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div[1]') == True:
                        sleep(1)
                        driver.find_element("xpath", '//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div[1]').click()
                        print("Clicked XP Multiplier")
                        sleep(1)
                        break
                    elif check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[2]/div[2]/div[1]') == False:
                        continue
                
                while i <2:
                    if check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[2]/div[2]') == True:
                        sleep(10)
                        coins = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.arts__modal___VpEAD-camelCase > div > div.styles__addTokenContainer___1Th4A-camelCase > div.styles__counterRow___1fheR-camelCase > div:nth-child(1) > div").text
                        xp = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.arts__modal___VpEAD-camelCase > div > div.styles__addTokenContainer___1Th4A-camelCase > div.styles__counterRow___1fheR-camelCase > div:nth-child(2) > div.styles__counterText___2hnWg-camelCase").text
                        print("\n")
                        print("Coins: " + coins)
                        print("XP: " + xp)
                        print("\n")
                        break
                    elif check_exists_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[2]/div[2]') == False:
                        continue
                
                driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.arts__modal___VpEAD-camelCase > div > div.styles__addTokenContainer___1Th4A-camelCase > div.styles__button___22rMT-camelCase.styles__hoverBlue___2zYb_-camelCase").click()
                print("Game Over")
    #!SECTION - End Game Function
    driver = uc.Chrome()
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
            pass

            #SECTION create Lobby
            
            sleep(2)
            driver.get(Blooket)
            print("what")
            while i < 2:
                print("testing")
                if check_exists_by_xpath('//*[@id="hostGame"]') == True:
                    print("found")
                    #select Gold
                    #driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div/div[1]/img').click()
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
                    
                    #FIXME - time doesnt seem to be changing, idk why, it seems to work beyond 7 but not before 7 
                    
                    #print("Time Set to " + BlooketTime + " minutes")
                    #sleep(2)
                    driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div[3]/div[3]/img').click()
                    sleep(2)
                    print("Turned on Gold")
                    driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div[4]/input').click()
                    GoldInput = driver.find_element('xpath', '//*[@id="app"]/div/div/div[3]/div[2]/div[4]/input')
                    GoldInput.send_keys(1000000000000)
                    sleep(2)
                    print("Set Gold to 1000000000000")
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
                elif check_exists_by_xpath('//*[@id="hostGame"]') == False:
                    print("not found")
                    continue
                
            print('Lobby Online :)')
            print('\n')
            pass
        #!SECTION create Lobby
        
        #SECTION join Lobby
                
            #ANCHOR Create Farmer
            driver.execute_script("window.open('');")
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://play.blooket.com/play")
            #print("Opened Bot " + str(bot) + "'s page")
            
            while i < 2: #ANCHOR Code loop
                if check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div[1]/input") == True:
                    codeEnter = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/form/div[2]/div[1]/input')
                    codeEnter.send_keys(code)
                    sleep(1)
                    codeEnter.send_keys(Keys.ENTER)
                    sleep(2)
                    break
                    
                elif check_exists_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[2]/div[1]/input") == False:
                    continue
                
                
            while i < 2: #ANCHOR Name loop
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
        #!SECTION join Lobby
            
            
        #SECTION Start Game
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
        #!SECTION Start Game
        
            #ANCHOR End Game call After Time
            BlooketTimeINT = int(BlooketTime) 
            BlooketTimeSTR = str(BlooketTime)
            start_time = threading.Timer(BlooketTimeINT,endGame)
            start_time.start()
            print("Game will end in " + BlooketTimeSTR + " Seconds")
            pass
            
            
        #SECTION Play Game
            sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            #allRight = 'let hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner; for (let i = 0; i < hack.stateNode.questions.length; i++) { hack.stateNode.questions[i].correctAnswers = hack.stateNode.questions[i].answers; hack.stateNode.forceUpdate(); }'
            #driver.execute_script(allRight)
            #print('AllRight.js Injected')
            while i < 2:
                driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                #print('hack Injected')
                stage = driver.execute_script("return hack.stateNode.state.stage")
                answer = driver.execute_script("return hack.stateNode.state.question.correctAnswers.toString()")
                choiceLength = driver.execute_script("return hack.stateNode.state.choices.length")
                
                stringStage = str(stage)
                print("stage: "+ stringStage)
                print("\n")
 
                if (choiceLength == 0) == True:
                    #print("No Choices")
                    pass
                
                #ANCHOR Question Stage
                if (stringStage == "question") == True:
                    print("answer: " + answer)
                    print("\n")
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
                
                #ANCHOR Prize Stage
                if (stringStage == "prize") == True:
                    driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                    choiceType1 = driver.execute_script("return hack.stateNode.state.choices[0].type")
                    choiceType2 = driver.execute_script("return hack.stateNode.state.choices[1].type")
                    choiceType3 = driver.execute_script("return hack.stateNode.state.choices[2].type")
                    choiceValue1 = driver.execute_script("return hack.stateNode.state.choices[0].val")
                    choiceValue2 = driver.execute_script("return hack.stateNode.state.choices[1].val")
                    choiceValue3 = driver.execute_script("return hack.stateNode.state.choices[2].val")
                    print("choice 1: " + choiceType1 + " " + str(choiceValue1))
                    print("choice 2: " + choiceType2 + " " + str(choiceValue2))
                    print("choice 3: " + choiceType3 + " " + str(choiceValue3))
                    
                    
                    #edit so that the Nothing type doesnt turn to 0
                    if choiceValue1 == None:
                        choiceValue1 = 0
                        pass
                    
                    if choiceValue2 == None:
                        choiceValue2 = 0
                        pass
                    
                    if choiceValue3 == None:
                        choiceValue3 = 0
                        pass
                  
                  
            #ANCHOR - Tests for if more than 1 choice is Gold or Multiply 
             
                #Gold
                    if (choiceType1 == "gold") == True and (choiceType2 == "gold") == True and (choiceType3 == "gold") == True:
                        if int(choiceValue1) > int(choiceValue2) and int(choiceValue1) > int(choiceValue3):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        
                        elif int(choiceValue1) < int(choiceValue2) and int(choiceValue2) > int(choiceValue3):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        
                        elif int(choiceValue1) < int(choiceValue3) and int(choiceValue2) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
                    if (choiceType1 == "gold") == True and (choiceType2 == "gold") == True:
                        if int(choiceValue1) > int(choiceValue2):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue1) < int(choiceValue2):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()   
                            continue
                        
                    if (choiceType1 == "gold") == True and (choiceType3 == "gold") == True:
                        if int(choiceValue1) > int(choiceValue3):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue1) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
                    if (choiceType2 == "gold") == True and (choiceType3 == "gold") == True:
                        if int(choiceValue2) > int(choiceValue3):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue2) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
                        
                        
                #Multiply 
                    if (choiceType1 == "multiply") == True and (choiceType2 == "multiply") == True and (choiceType3 == "multiply") == True:
                        if int(choiceValue1) > int(choiceValue2) and int(choiceValue1) > int(choiceValue3):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        
                        elif int(choiceValue1) < int(choiceValue2) and int(choiceValue2) > int(choiceValue3):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        
                        elif int(choiceValue1) < int(choiceValue3) and int(choiceValue2) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                  
                    if (choiceType1 == "multiply") == True and (choiceType2 == "multiply") == True:
                        if int(choiceValue1) > int(choiceValue2):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue1) < int(choiceValue2):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
                    if (choiceType1 == "multiply") == True and (choiceType3 == "multiply") == True:
                        if int(choiceValue1) > int(choiceValue3):
                            print("choice 1 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue1) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
                    if (choiceType2 == "multiply") == True and (choiceType3 == "multiply") == True:
                        if int(choiceValue2) > int(choiceValue3):
                            print("choice 2 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        elif int(choiceValue2) < int(choiceValue3):
                            print("choice 3 is greater")
                            print("\n")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    
  
                    
                    
                    
            #ANCHOR - Tests if only 1 choice is Gold or Multiply
            
                #Choice 1
                    if (choiceType1 == "divide") == True:
                        if choiceType1 == "divide" and choiceType2 != "gold" or choiceType2 != "multiply"  or choiceType2 != "nothing" and choiceType3 != "gold" or choiceType3 != "multiply" or choiceType3 != "nothing":
                            print("choice 1 is divide and all thats left") 
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        else:
                            pass
                    else:
                        pass
                    if (choiceType1 == "take") == True:
                        pass  
                    if (choiceType1 == "swap") == True:
                        pass                       
                    if (choiceType1 == "multiply") == True:
                        if (choiceType1 == "multiply") == True and (choiceType2 == "multiply") == False and (choiceType3 == "multiply") == False:
                            print("choice 1 is multiply")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                    else:
                        pass        
                    
                #FIXME - if choice 1 is gold and the others are multiply, it will choose choice 1 instead of 2 or 3        
                #REVIEW - SHOULD BE FIXED NOW          
                    if (choiceType1 == "gold") == True: 
                        if (choiceType1 == "gold") == True and (choiceType2 == "multiply") == True or (choiceType3 == "multiply") == True:
                            if choiceValue2 > choiceValue3:
                                print("choice 2 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
                            elif choiceValue2 < choiceValue3:
                                print("choice 3 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
       
                        else:
                            print("choice 1 is gold")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                    
                    if (choiceType1 == "nothing") == True:
                        if (choiceType1 == "nothing") == True and (choiceType2 == "swap") == True or (choiceType2 == "take") == True or (choiceType2 == "divide") == True and (choiceType3 == "swap") == True or (choiceType3 == "take") == True or (choiceType3 == "divide") == True:
                            print("choice 1 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                            continue
                        else:
                            print("choice 1 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                        
                    
                #Choice 2
                    if (choiceType2 == "divide") == True:
                        if choiceType2 == "divide" and choiceType1 != "gold" or choiceType1 != "multiply"  or choiceType1 != "nothing" and choiceType3 != "gold" or choiceType3 != "multiply" or choiceType3 != "nothing":
                            print("choice 2 is divide and all thats left")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()   
                            continue
                        else:
                            pass
                    else:
                        pass
                    if (choiceType2 == "take") == True:
                        pass  
                    if (choiceType2 == "swap") == True:
                        pass                       
                    if (choiceType2 == "multiply") == True:
                        if (choiceType1 == "multiply") == False and (choiceType2 == "multiply") == True and (choiceType3 == "multiply") == False:
                            print("choice 2 is multiply")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()   
                            continue                       
                    else:
                        pass
                    if (choiceType2 == "gold") == True:
                        if (choiceType2 == "gold") == True and (choiceType1 == "multiply") == True or (choiceType3 == "multiply") == True:
                            if choiceValue1 > choiceValue3:
                                print("choice 1 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
                            elif choiceValue1 < choiceValue3:
                                print("choice 3 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
                        else:
                            print("choice 2 is gold")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                    
                    if (choiceType2 == "nothing") == True:
                        if (choiceType2 == "nothing") == True and (choiceType1 == "take") == True or (choiceType1 == "swap") == True or (choiceType1 == "divide") == True and (choiceType3 == "take") == True or (choiceType3 == "swap") == True or (choiceType3 == "divide") == True:
                            print("choice 2 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                            
                        else:
                            print("choice 2 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                        
                #Choice 3
                    if (choiceType3 == "divide") == True:                          
                        if choiceType3 == "divide" and choiceType1 != "gold" or choiceType1 != "multiply"  or choiceType1 != "nothing" and choiceType2 != "gold" or choiceType2 != "multiply" or choiceType2 != "nothing":
                            print("choice 3 is divide and all thats left")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                        else: 
                            pass
                    if (choiceType3 == "take") == True:
                        pass  
                    if (choiceType3 == "swap") == True:
                        pass                       
                    if (choiceType3 == "multiply") == True:
                        if (choiceType1 == "multiply") == False and (choiceType2 == "multiply") == False and (choiceType3 == "multiply") == True:
                            print("choice 3 is multiply")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                    if (choiceType3 == "gold") == True:
                        if (choiceType3 == "gold") == True and (choiceType1 == "multiply") == True or (choiceType2 == "multiply") == True:
                            if choiceValue1 > choiceValue2:
                                print("choice 1 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#chest1").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
                            elif choiceValue1 < choiceValue2:
                                print("choice 2 is greater")
                                print("\n")
                                driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice2___1aP2D-camelCase").click()
                                sleep(1)
                                driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                                continue
                        else:
                            print("choice 3 is gold")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass 
                    if (choiceType3 == "nothing") == True:
                        if (choiceType3 == "nothing") == True and (choiceType1 == 'take') == True or (choiceType1 == 'swap') == True or (choiceType1 == "divide") == True and (choiceType2 == 'take') == True or (choiceType2 == 'swap') == True or (choiceType2 == "divide") == True:
                            print("choice 3 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                        else:
                            print("choice 3 is nothing")
                            driver.find_element(By.CSS_SELECTOR, "#claimButton > div > div.styles__choice3___2L6Q--camelCase").click()
                            sleep(1)
                            driver.find_element(By.CSS_SELECTOR, "#app > div > div").click() 
                            continue
                    else:
                        pass
                pass
                
                #ANCHOR - Feedback Stage
                if (stringStage == "feedback") == True:
                    driver.execute_script('hack = Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner;')
                    driver.find_element(By.CSS_SELECTOR, "#app > div > div").click()
                    continue
            
        #!SECTION Play Game
            
    except Exception as e:
        print(e)