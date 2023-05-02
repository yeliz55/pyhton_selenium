from instagramUserInfo import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import *


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username_input = self.browser.find_element(
            By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        username_input.send_keys(self.username)
        password_input = self.browser.find_element(
            By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        followersLink = self.browser.find_element(
            By.XPATH, "//*[@id='mount_0_0_QM']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followersLink.click()

        followerList = self.browser.find_elements(
            By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
            
        for i in followerList:
            print(f"https://instagram.com/{i.text}/")

       # toplu yoruma almak ıcın ıstedıgın yerı sec ctrl+k+c
       # toplu yorumdan kaldırmak icin istedigin yeri sec ctrl+k+u


       


instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()
