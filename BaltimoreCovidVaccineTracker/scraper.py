from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def scrape():
	url = 'https://coronavirusvaccineoutreach-bc-gis.hub.arcgis.com/#statistics'

	print("Opening browser")
	fire_fox_options = webdriver.FirefoxOptions()
	fire_fox_options.headless = True
	driver = webdriver.Firefox(options=fire_fox_options)

	print("Navigating to webpage")
	driver.get(url)

	print("Waiting for Javascript to load (20 second timeout)")
	try: 
		element = WebDriverWait(driver, 20).until(
			expected_conditions.presence_of_element_located((By.CLASS_NAME, "ss-value")))
	except TimeoutException as e:
		print("Javascript didn't load.  Defaulting to no vaccinations")
		return 0, 0
	except Exception as e:
		print("Something other than Javascript not loading went wrong. Defaulting to no vaccinations. e=", e)
		return 0, 0
	else:
		# num_first_str = driver.find_element_by_xpath(
		# 	"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[2]/div[2]/div/div[2]/span[1]").text
		# num_second_str = driver.find_element_by_xpath(
		# 	"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[4]/div[2]/div/div[2]/span[1]").text
		percent_first_str = driver.find_element_by_xpath(
			"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[3]/div/div/div/div").text
		percent_second_str = driver.find_element_by_xpath(
			"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[5]/div/div/div/div").text

		print(percent_first_str + " have had their first shot.")
		print(percent_second_str + " have had their second shot.")

		return float(percent_first_str.replace('%', '')), float(percent_second_str.replace('%', ''))
