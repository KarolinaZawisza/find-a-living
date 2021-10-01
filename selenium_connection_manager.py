from selenium import webdriver

class SeleniumConnectionManager:

    cdp = 'C:\Development\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=cdp)

    @staticmethod
    def connect_to_google(driver):
        driver.get('https://forms.gle/Ymi7uyhk1MsxUWC38')