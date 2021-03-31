import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape():
	URL = 'https://coronavirusvaccineoutreach-bc-gis.hub.arcgis.com/#statistics'

	print("Opening browser")
	fireFoxOptions = webdriver.FirefoxOptions()
	fireFoxOptions.headless = True
	driver = webdriver.Firefox(options=fireFoxOptions)

	print("Navigating to webpage")
	driver.get(URL)

	print("Waiting for JS to load (20 second timeout)")
	try: 
		element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ss-value"))) 
	except:
		print("JS Didn't Load")
	# else
		
	numFirstStr = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[2]/div[2]/div/div[2]/span[1]").text
	numSecondStr = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[4]/div[2]/div/div[2]/span[1]").text
	percentFirstStr = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[3]/div/div/div/div").text
	percentSecondStr = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[5]/div/div/div/div").text

	print(percentFirstStr + " have had their first shot.")
	print(percentSecondStr + " have had their second shot.")

	return float(percentFirstStr.replace('%','')), float(percentSecondStr.replace('%','')) 
