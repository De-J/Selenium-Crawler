# Selenium-Crawler

This repository contains python scripts for scraping data, using Selenium, from Flipkart and Amazon.

### Problems Encountered:
1) Search results are displayed differently depending upon the product searched.
For example, on both Amazon and Flipkart, searching for electronics like mobiles or laptops yields only 1 product per row. On the other hand, clothing items or food products tend to be displayed 4 products per row.
Since, the results are displayed differently for different products, the HTML code in DOM changes for different products.

Solution: In Flipkart search results, look only for  ```<div>``` tags with ```data-id``` attribute since each of these tags indicates presence of a product.
```python
cols = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
```

#### Features implemented: 
1) Take search name as input and generate output text file.

2) Mimicking human behaviour/evading bot detection using [Selenium-stealth](https://pypi.org/project/selenium-stealth/) (not tested fully).

```python
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
```
Launching the chromedriver with above specifications helps in preventing selenium detections. 

3) Evading bot detection by adding cookies (not tested fully)
```python
driver.add_cookie()
```
#### Improvements yet to be done:
1) Creating a text file handling function and calling it in main module.
2) Treating product attributes fetched from Amazon or Flipkart as attributes of a class object (Object-Oriented Model)
3) To further evade bot detection, recompile the source code of chromedriver by replacing instances of ```cdc_``` string according to this [discussion](https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver).
