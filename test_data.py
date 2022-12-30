from ssl import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from config import CHROME_PROFILE_PATH
import logging
from BaseClass import BaseClass 


class Testone(BaseClass):

    Issue_bots=[]
    Working_bots=[]
    whatsapp_login=True
    
    def test_WhatsappBotSanity(self):

        log = self.getLogger()
        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)

        service_obj = Service("C:/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=options)

        names=["Curatio Bot", "Metropolis Healthcare Bot", "Motilal Oswal Bot", "SOAL Bot", "Goapptiv Piesa Bot", "iTAX Service Bot", 
        "Nanhi Kali Bot", "Madhavbaug Bot", "Sugam Solar Bot", "Sanctum Bot", "Cherise Tapri Chatbot", "UPL Farmer Bot", 
        "UPL Retailer Prod Bot"]
        
        driver.get("https://www.whatsapp.com/")
        driver.find_element(By.XPATH, '//h5[@class="_9vd5"][.="WHATSAPP WEB"]').click()
        
        try:
            wait = WebDriverWait(driver,30)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@title='Search input textbox']")))


            for name in names:

                try:
                    wait = WebDriverWait(driver,30)
                    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[title='{}']".format(name))))
                except Exception as e:
                    log.info("Issue while loding whatsapp or {} name does not exist".format(name))     
                try:
                    driver.find_element(By.CSS_SELECTOR, "span[title='{}']".format(name)).click()
                    message_box = (By.CSS_SELECTOR, "p[class='selectable-text copyable-text']")
                    message = (By.CSS_SELECTOR, "p[class='selectable-text copyable-text']")
                    send_button = (By.CSS_SELECTOR, "span[data-testid='send']")
                    last_reply = (By.XPATH, '(//div[@class="ItfyB _3nbHh"] //div[@class="copyable-text"] //span[@dir="ltr"])[last()]')

                    driver.find_element(*message_box).click()
                    time.sleep(2)
                    driver.find_element(*message).send_keys("Hi")
                    driver.find_element(*send_button).click()
                    time.sleep(15)
                    Last_text = driver.find_element(*last_reply).text

                    if name == "Curatio Bot" or name == "Metropolis Healthcare Bot" or name == "Motilal Oswal Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Please Select Option"
                    if name == "SOAL Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Reply with the option number (Eg. 2 for Admission Process) to select that option."
                    elif name == "Goapptiv Piesa Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Welcome to GoApptiv! India’s fastest growing end-to-end business"
                    elif name == "iTAX Service Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "1. New User"
                    elif name == "Nanhi Kali Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "1. Stories of the month"
                    elif name == "Madhavbaug Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "We are unable to fetch your previous details."
                    elif name == "Sugam Solar Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Please select"
                    elif name == "Sanctum Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "All agents"
                    elif name == "Cherise Tapri Chatbot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Welcome to Cherise. Kindly type in your name."
                    elif name == "UPL Farmer Bot":
                        try:
                            log.info(" {} is the last text".format(Last_text))
                            Actual_text = "1. Connect to Live Chat Agent"
                            if Last_text==Actual_text:
                                pass
                            else:
                                time.sleep(30)
                                Last_text = driver.find_element(*last_reply).text
                        except Exception as e:
                            pass
                    elif name == "UPL Retailer Prod Bot":
                        log.info(" {} is the last text".format(Last_text))
                        Actual_text = "Namaskar, nurture.farm care main apka swagat" 
                    

                    if Actual_text in Last_text:
                        log.info(" {} last line matched".format(name))
                        Testone.Working_bots.append(name)
                    else:
                        log.error(" {} does not match".format(name))
                        Testone.Issue_bots.append(name)

                except Exception as e:
                    log.error(" Issue seen in {}".format(name))
                    Testone.Issue_bots.append(name)
        except Exception as e:
            log.error("Whatsapp not responding try again or try after turning on the phone whatsapp")
            Testone.whatsapp_login = False


    def test_WebBotSanity(self):

        log = self.getLogger()
        service_obj = Service("C:/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)  

        websites=["https://curatiohealthcare.com/","https://us.engagelybots.ai/chatbot/?botId=xxjElr8_obyl"]

        for website in websites:
            WebBot_active=False
            driver.get("{}".format(website))
            
            if website == "https://curatiohealthcare.com/":
                try:
                    wait = WebDriverWait(driver,15)
                    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//iframe[@id='iframe']")))
                    driver.find_element(By.XPATH, "//iframe[@id='iframe']").click()
                    WebBot_active=True
                    Testone.Working_bots.append("Curatio Web Bot")
                except Exception as e:
                    Testone.Issue_bots.append("Curatio Web Bot")
                    pass
            elif website == "https://us.engagelybots.ai/chatbot/?botId=xxjElr8_obyl":
                try:
                    wait = WebDriverWait(driver,15)
                    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='image_container ng-trigger ng-trigger-botIconAnimation ng-tns-c1-0 ng-star-inserted']")))
                    driver.find_element(By.XPATH, "//div[@class='image_container ng-trigger ng-trigger-botIconAnimation ng-tns-c1-0 ng-star-inserted']").click()
                    WebBot_active=True
                    Testone.Working_bots.append("ARC Fertility Bot")
                except Exception as e:
                    Testone.Issue_bots.append("ARC Fertility Bot")
                    pass
                    
            if WebBot_active==True:
                log.info(" {} working fine".format(website))
            else:
                log.error(" Issue seen in {}".format(website))


    def test_Results(self):
        log = self.getLogger()
        Issue_counter = len(Testone.Issue_bots)
        Working_counter = len(Testone.Working_bots)

        if Issue_counter==0 and Testone.whatsapp_login==True:
            log.info("All bots are working fine")
        elif Issue_counter>=1 and Testone.whatsapp_login==True:
            log.warning("Following {} Bot is impacted {} ".format(Issue_counter, Testone.Issue_bots))
        else:
            log.warning("Whatsapp_login not responding try again or try after turning on the phone whatsapp")

        log.info("Following {} Bots is working {} ".format(Working_counter, Testone.Working_bots))


            
            
        
    


