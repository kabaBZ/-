from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_size():#获取页面大小
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

#appium设置参数
cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "noReset": True,
    "unicodekeyboard": True,
    "resetkeyboard": True,
    "automationName": "UIAutomator1"
}

#定义驱动
driver = webdriver.Remote('http://localhost:4723/wd/hub',cap)

#点击搜索按钮
try :
    if WebDriverWait(driver,10).until(lambda x:x. find_element_by_id('com.ss.android.ugc.aweme:id/c0=')):
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/c0=').click()
except:
    pass

#点击搜索框，输入id，点击搜索
if WebDriverWait(driver,2).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/et_search_kw')):
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/et_search_kw').click()
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/et_search_kw').send_keys('WYB.')
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/k4g').click()

#点击id
if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath('//android.view.View[@content-desc="UNIQ-王一博"]')):
    driver.find_element_by_xpath('//android.view.View[@content-desc="UNIQ-王一博"]').click()

#点击粉丝数
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/c6c')):
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/c6c').click()

time.sleep(2)

l = get_size()#定义指针位置
x1 = int(l[0]*0.5)
y1 = int(l[1]*0.9)
y2 = int(l[1]*0.15)

while True:
    if '没有更多了'in driver.page_source:#滑动结束条件
        break
    else:
        driver.swipe(x1,y1,x1,y2)#滑动操作