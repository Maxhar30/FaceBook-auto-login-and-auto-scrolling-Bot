#!/bin/python
from selenium import webdriver
import time

usr = "email@gmail.com"
pas = "Password"

browser = webdriver.Chrome()
browser.get('https://en-gb.facebook.com/')
user = browser.find_element_by_css_selector("#email")
user.clear()
user.send_keys(usr)	
passwd = browser.find_element_by_css_selector("#pass")
passwd.clear()
passwd.send_keys(pas)	
btn = browser.find_element_by_name("login").click()
delay = 5

y = 100
for timer in range(0,5000):
    browser.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 100  
    time.sleep(1)

#Coded by Cgravity(Mxhr-The-Night-Hunt3r)