from selenium import webdriver
webdriverPath="C:\\Users\ASUS\Downloads\chromedriver_win32 (1)"
path="C:\Program Files\chromedriver"
driver = webdriver.Chrome(path)
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
contact = input()
message = "Write your  message here"
driver.find_element_by_css_selector("span[title='" + (f"{contact}") + "']").click()
inputString = (f"{message}")
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()