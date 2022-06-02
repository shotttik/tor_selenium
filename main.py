from selenium import webdriver
import os
import time

sudoPassword = 'kali'
command = 'service tor restart'

PROXY = "socks5://localhost:9050"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)

# FIRST TIME
driver = webdriver.Chrome(
    executable_path="./chromedriver", options=options)
# driver.get("http://check.torproject.org")
driver.get("https://2ip.ru")
os.system(f'echo {sudoPassword}|sudo -S {command}')
os.system(command)
time.sleep(10)
driver.close()

time.sleep(2)

# SECOND TIME
driver = webdriver.Chrome(
    executable_path="./chromedriver", options=options)
# driver.get("http://check.torproject.org")
driver.get("https://2ip.ru")
os.system(f'echo {sudoPassword}|sudo -S {command}')
os.system(command)
time.sleep(10)
driver.close()

time.sleep(2)
# Third TIME
driver = webdriver.Chrome(
    executable_path="./chromedriver", options=options)
# driver.get("http://check.torproject.org")
driver.get("https://2ip.ru")
os.system(f'echo {sudoPassword}|sudo -S {command}')
os.system(command)
time.sleep(10)
driver.close()
