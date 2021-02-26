from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
from selenium import webdriver
        
capabilities = {
    "browserName": "chrome",
    "browserVersion": "64.0",
    "selenoid:options": {
        # "enableVNC": True,
        "enableVideo": True
    }
}

driver = webdriver.Remote(
    command_executor="http://45.15.25.151:4444/wd/hub",
    desired_capabilities=capabilities)

# Welcome to Rocket Software
@allure.severity(allure.severity_level.NORMAL)
def test_youtube_like_on_video():
    driver.get("https://www.youtube.com/")
    print('Typing')
    assert True

