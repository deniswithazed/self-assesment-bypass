from selenium import webdriver

chromedriver_location = "C:/Users/deniz/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(chromedriver_location)

driver.get('https://www.tandia.com/selfcheck')

start = '//*[@id="433f9284-9839-403b-94ba-bafc445a6858"]/div/div/a'

driver.find_element_by_xpath(start).click() 

f_name = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/input'

driver.find_element_by_xpath(f_name).send_keys("Deniz")

l_name = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/input'

driver.find_element_by_xpath(l_name).send_keys("Saygili")

location = '//*[@id="SelectId_0_placeholder"]/span'

driver.find_element_by_xpath(location).click()

milton = '//*[@id="SelectId_0"]/div[2]/div[11]/div/span'

driver.find_element_by_xpath(milton).click()

none_0 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_0).click()


nb_0 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button/div'

driver.find_element_by_xpath(nb_0).click()

none_1 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_1).click()

nb_1 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div'

driver.find_element_by_xpath(nb_1).click()

none_2 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_2).click()

nb_2 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div'

driver.find_element_by_xpath(nb_2).click()

none_3 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_3).click()

nb_3 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div'

driver.find_element_by_xpath(nb_3).click()

none_4 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_4).click()

nb_4 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div'

driver.find_element_by_xpath(nb_4).click()

none_5 = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'

driver.find_element_by_xpath(none_5).click()

submit = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div'

driver.find_element_by_xpath(submit).click()


