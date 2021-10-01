from selenium import webdriver

class SeleniumConnectionManager:

    cdp = 'C:\Development\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=cdp)

    @staticmethod
    def connect_to_zillow(driver):
        driver.get('https://www.zillow.com/homes/for_rent/')