from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from csv import DictReader

def getCookies(file):
    with open(file, encoding="utf-8-sig") as f:
        dict = DictReader(f)
        dictlist = list(dict)

    return dictlist

def launch():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chr_options)
    page = driver.get("https://www.grailed.com")
    
    # links = driver.find_elements(by=By.CSS_SELECTOR, value="a")
    # for link in links:
    #     text = link.text
    #     print(text)

    driver.find_element(by=By.LINK_TEXT, value="SHOP MENSWEAR").click()

    cookieslist = getCookies("/cookies.csv")

    for cookie in cookieslist:
        driver.add_cookie(cookie)

    driver.refresh()

launch()