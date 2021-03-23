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

# Path to your webdriver
browser = webdriver.Chrome('C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project\\chromedriver',options=options)
browser.implicitly_wait(10)
browser.get('https://covid.cdc.gov/covid-data-tracker/#vaccination-demographic')

#Using wait because the elements did not load yet. 
#Explicit Wait - Waits until condition is met 
try:
    # Race Ethnicity
    re_fully_vaccinated_bttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export040"]'))
    )
    re_fully_vaccinated_bttn.send_keys(Keys.ENTER)
    data_re_fully_vaccinated_bttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-040"]'))
    )
    data_re_fully_vaccinated_bttn.send_keys(Keys.ENTER)

    #Age Group
    age_fully_vaccinated_bttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export010"]'))
    )
    age_fully_vaccinated_bttn.send_keys(Keys.ENTER)
    data_age_fully_vaccinated_bttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-010"]'))
    )
    data_age_fully_vaccinated_bttn.send_keys(Keys.ENTER)

    #Sex group
    sex_fully_vaccinated_bttn =  WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="demo-export009"]'))
    )
    sex_fully_vaccinated_bttn.send_keys(Keys.ENTER)
    data_sex_fully_vaccinated_bttn =  WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dwn-data-009"]'))
    )
    data_sex_fully_vaccinated_bttn.send_keys(Keys.ENTER)
finally:
    browser.close()



# re_fully_vaccinated_bttn = browser.find_element_by_xpath('//*[@id="demo-export040"]').send_keys(Keys.ENTER)
# data_re_fully_vaccinated_bttn = browser.find_element_by_id('//*[@id="dwn-data-040"]').send_keys(Keys.ENTER)
# print('Testings', re_fully_vaccinated_bttn)


