from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def scrape(verbose=True):
	"""Scrape the below url for the percentage of population that has received the
	first and second vaccination doses in baltimore.  Return the values as floats.

	If verbose is True, useful console output will be printed.

	Upon error preventing the scrape we default to no vaccinations

	"""

	url = 'https://coronavirusvaccineoutreach-bc-gis.hub.arcgis.com/#statistics'
	percent_first_shot = 0
	percent_second_shot = 0

	if verbose: print("Opening browser")
	fire_fox_options = webdriver.FirefoxOptions()
	fire_fox_options.headless = True
	driver = webdriver.Firefox(options=fire_fox_options)

	if verbose: print("Navigating to webpage")
	driver.get(url)

	if verbose: print("Waiting for Javascript to load (20 second timeout)")
	try: 
		element = WebDriverWait(driver, 20).until(
			expected_conditions.presence_of_element_located((By.CLASS_NAME, "ss-value")))
	except TimeoutException as e:
		if verbose: print("Javascript didn't load.  Defaulting to no vaccinations")
	except Exception as e:
		if verbose: print("Something other than Javascript not loading went wrong. Defaulting to no vaccinations. e=", e)
	else:
		if verbose: print("Javascript loaded")

		# num_first_str = driver.find_element_by_xpath(
		# 	"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[2]/div[2]/div/div[2]/span[1]").text
		# num_second_str = driver.find_element_by_xpath(
		# 	"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[4]/div[2]/div/div[2]/span[1]").text
		percent_first_str = driver.find_element_by_xpath(
			"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[3]/div/div/div/div").text
		percent_second_str = driver.find_element_by_xpath(
			"/html/body/div[6]/div[2]/div/div[1]/div[3]/div/div/section[3]/div/div[5]/div/div/div/div").text

		if verbose: print("Scrape complete")
		percent_first_shot = float(percent_first_str.replace('%', ''))
		percent_second_shot = float(percent_second_str.replace('%', ''))
	finally:
		if verbose: print("Closing driver")
		driver.close()

	return percent_first_shot, percent_second_shot
