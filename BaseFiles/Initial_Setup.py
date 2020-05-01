from selenium.webdriver import Chrome

def open_url():
    global driver
    path = "C:\\Users\\Viral Parmar\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    return driver

def close_url():
    driver.close()