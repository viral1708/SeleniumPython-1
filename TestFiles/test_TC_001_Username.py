from selenium.webdriver import Chrome
#from BaseFiles import Initial_Setup

def test_UserName():
  #  driver1 = Initial_Setup.open_url()
    path = "C:\\Users\\Viral Parmar\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    driver.find_element_by_name("fld_username").send_keys("Hello")
    driver.close()


