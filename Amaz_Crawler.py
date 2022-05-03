from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

product_name = input()
#number_of_fields = int(input())

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

service = ChromeService(executable_path = r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)
url = f"https://www.amazon.in/s?k={product_name}"
driver.get(url)


product = {}

cols = driver.find_elements(By.CSS_SELECTOR, "a[class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")



i = 1
for col in cols:    
    if (i > 2):
        break
    

    col.click()
    driver.switch_to.window(driver.window_handles[i])
    
    name = driver.find_element(By.ID, "productTitle")
    product.update({"Name" : name.text})
    driver.find_element(By.TAG_NAME, "h2")

    #brand = driver.find_element(By.ID, "bylineInfo")
    
        #product.update({"Brand" : brand.text})
        results = driver.find_element(By.CSS_SELECTOR, "div[class = 'row _1v8OXw']")
        specs = results.find_elements(By.CSS_SELECTOR, "div[class = 'row']")  
    
    else:
        product.update({"Name" : span[0].text})
        specs = driver.find_elements(By.CSS_SELECTOR, "tr[class = '_1s_Smc row']")
    
    specs = specs[:number_of_fields] 
    for spec in specs:
        attribute = spec.find_element(By.CSS_SELECTOR, "td[class = '_1hKmbr col col-3-12']").text
        attribute_value = spec.find_element(By.TAG_NAME, "li").text
        product.update({attribute : attribute_value})
    i += 1
    driver.switch_to.window(driver.window_handles[0])
    print(product)




time.sleep(20)
driver.quit()
'''
