from selenium import webdriver
from selenium.webdriver.chrome.options import Options   
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Add google chrome download preferences to choose where the files will be stored when downloaded.
options = webdriver.ChromeOptions()
# Needed to change path and add two backslashes instead. 
prefs = {'download.default_directory': 'C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project'}
options.add_experimental_option('prefs',prefs)

driver_path = 'C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project\\chromedriver'
# Path to your webdriver
browser = webdriver.Chrome(driver_path,options=options)
# Open website
browser.get('https://covid.cdc.gov/covid-data-tracker/#vaccination-demographic')


#Using wait because the DOM has not all elements yet. 
#Explicit Wait - Waits until condition is met 
wait = WebDriverWait(browser,10)
try:
    # Race Ethnicity--------------------------------------------------------
    re_fully_vaccinated_bttn = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export040"]'))
    ).click()
    data_re_fully_vaccinated_bttn = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-040"]'))
    ).click()
    #Age Group--------------------------------------------------------------
    age_fully_vaccinated_bttn = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export010"]'))
    ).click()
    data_age_fully_vaccinated_bttn = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-010"]'))
    ).click()

    # Sex group--------------------------------------------------------------
    sex_fully_vaccinated_bttn =  wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export009"]'))
    ).click()
    data_sex_fully_vaccinated_bttn =  wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-009"]'))
    ).click()
finally:
    browser.close()



