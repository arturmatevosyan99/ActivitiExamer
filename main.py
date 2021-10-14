from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from webdriver_manager.driver import Driver

USERNAME = "artur.matevosyan2"
PASS = "!Savn7777"






def authorization(username, password):
    userName = USERNAME
    password = PASS

    userName_field = driver.find_element_by_id("input-18").send_keys(userName)
    password_field = driver.find_element_by_id("input-21").send_keys(password)
    button = driver.find_element_by_xpath('//*[@id="activity-manager-login-form-card-login-button"]/span').click()


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://activities.am.tumo.world/")


time.sleep(1)
# input-18

authorization(USERNAME,PASS)
time.sleep(5)
button = driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(5)
activityButton = driver.find_element_by_id("input-56").send_keys("Elements of programming")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="list-56"]/div/div/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div[2]/main/div/div/div/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/div/span').click()
time.sleep(5)
link = driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div/a').get_attribute("href")
time.sleep(5)

if link.find("level=8") != -1:
    levelWin = False
    print(link)
    finishX = "-141"
    finishY = "291"
    # finish -141 291
    driverLevel = webdriver.Chrome(ChromeDriverManager().install())
    driverLevel.get(link)

    x = driverLevel.find_element_by_id('pegman').get_attribute('x')
    y = driverLevel.find_element_by_id('pegman').get_attribute('y')
    driverLevel.find_element_by_id('runButton').click()
    time.sleep(5)
    runnigTime = 0
    breakeFlag = False
    while True:
        time.sleep(0.2)
        print(x)
        print(y)
        print(runnigTime)
        runnigTime += 0.2
        x = driverLevel.find_element_by_id('pegman').get_attribute('x')
        y = driverLevel.find_element_by_id('pegman').get_attribute('y')

        
        if x == finishX and y == finishY:
            levelWin = True
            break


        if runnigTime >= 40:
            breakeFlag = True
            break


    driverLevel.quit()
    print(levelWin, x,y , breakeFlag)


if levelWin:
    driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/button[2]').click()

time.sleep(100)


driver.quit()



