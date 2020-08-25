from selenium import webdriver

# open a sample browser and navigate it
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\chromedriver.exe')
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# extract lists of "buyers" and "prices" based on xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

#printout all of the buyers and prices are current page
num_page = len(buyers)
for i in range(num_page):
    print(buyers[i].text + " : " + prices[i].text)

# clean up (close browser once task is completed)
driver.close()
