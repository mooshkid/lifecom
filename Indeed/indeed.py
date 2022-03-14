from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#chrome options
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 9')
driver = webdriver.Chrome(options=options)

#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://employers.indeed.com/j#cdjobs")

#loop counter
count = 1
#start timer
start = time.time()

#start loop (64 posts)
table = driver.find_element(By.ID, 'cdjobstab')
for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
    for ahref in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a'):
        print('Starting(' + str(count) + '):' + ahref.text)
        count +=1

        #open post in new tab
        ahref.send_keys(Keys.CONTROL + Keys.ENTER)
        #switch to tab1
        driver.switch_to.window(driver.window_handles[1])

        #status button
        time.sleep(10)
        statusButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-0-toggle-button"]')))
        #close job
        statusButton.send_keys(Keys.ENTER + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        print('Closed')

        #close & switch tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)


    for label in row.find_elements(By.CSS_SELECTOR, 'td > label'):
        label.click()

        #copy button
        copyButton = driver.find_element(By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/div/div[2]/a[2]')
        copyButton.send_keys(Keys.CONTROL + Keys.ENTER)
        print('Copying...')
        #uncheck box
        label.click()
        #switch to tab1
        driver.switch_to.window(driver.window_handles[1])

        #confirm button
        time.sleep(1)
        confirmButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirm-button-in-preview"]')))
        confirmButton.click()

        #don't optimize
        noOptimize = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniqueId1"]')))
        noOptimize.click()
        print('Finished')

        #close & switch tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

#print elapsed time
end = time.time()
tt = end - start
print('Task Completed in: ' + str(tt) + ' seconds')

driver.close()