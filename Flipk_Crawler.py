from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

product_name = input()
number_of_fields = int(input())

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

'''
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
'''



service = ChromeService(executable_path = r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)
url = f"https://www.flipkart.com/search?q={product_name}"
driver.get(url)


product = {}

cols = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")


i = 1
j = 0
flag = 0
with open("Searches.txt", 'a') as tf:
    for col in cols:    
        if (i > 2):
            break

        link = col.find_element(By.TAG_NAME, 'a')
        link.click() #to execute the click the driver needs to be on the link page
        driver.switch_to.window(driver.window_handles[i])
        
        h1 = driver.find_element(By.TAG_NAME, "h1")
        span = h1.find_elements(By.TAG_NAME, "span")
        
        if (len(span) > 1):
            product.update({"Brand" : span[0].text})
            product.update({"Name" : span[1].text})
            results = driver.find_element(By.CSS_SELECTOR, "div[class = 'row _1v8OXw']")
            specs = results.find_elements(By.CSS_SELECTOR, "div[class = 'row']")  
        
        else:
            product.update({"Name" : span[0].text})
            specs = driver.find_elements(By.CSS_SELECTOR, "tr[class = '_1s_Smc row']")
            flag = 1
        specs = specs[:number_of_fields] 
        
        for spec in specs:
            if flag == 1:
                attribute = spec.find_element(By.CSS_SELECTOR, "td[class = '_1hKmbr col col-3-12']").text
                attribute_value = spec.find_element(By.TAG_NAME, "li").text
                product.update({attribute : attribute_value})
            else:
                attribute = spec.find_element(By.CSS_SELECTOR, "div[class = 'col col-3-12'")
                attribute_value = spec.find_element(By.CSS_SELECTOR, "div[class = 'col col-9-12']")
                product.update({attribute : attribute_value})
        i += 1
        driver.switch_to.window(driver.window_handles[0])
        
        
        if j == 0:
            for key in product.keys():
                tf.write(key)
                tf.write("\t"*4)
            tf.write('\n')
        for value in product.values():
            tf.write(value)
            tf.write("\t"*4)
        tf.write('\n')
        j += 1
        print(product)
    

time.sleep(20)
driver.quit()
