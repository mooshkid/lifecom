from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sys
import logging

#logging config
path = os.getcwd()
logPath = os.path.join(path, "logs/indeed_life.log")

logging.basicConfig(
    level=logging.INFO,
    format=u'%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(logPath, encoding='utf8'),
        logging.StreamHandler()
    ]
)
class LoggerWriter:
    def __init__(self, level):
        self.level = level
    def write(self, message):
        if message != '\n':
            self.level(message)
    def flush(self): pass
log = logging.getLogger(__name__)
sys.stdout = LoggerWriter(log.debug)
sys.stderr = LoggerWriter(log.error)

#chrome options
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 8')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

#launch URL
driver.get("https://employers.indeed.com/j#cdjobs")

#loop counter
count = 1
#start timer
start = time.time()

#start loop
table = driver.find_element(By.ID, 'cdjobstab')
for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
    for aTag in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a'):
        #location name
        for location in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)'):
            locText = location.text
        log.info('Starting(' + str(count) + '): ' + aTag.text + ' - ' + locText)
        count +=1

        #open post in new tab
        aTag.send_keys(Keys.CONTROL + Keys.ENTER)
        #switch to tab1
        driver.switch_to.window(driver.window_handles[1])

        #status button
        time.sleep(4)
        statusButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-0-toggle-button"]')))
        #close job
        statusButton.send_keys(Keys.ENTER + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        log.info('Closed')

        #close & switch tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)


    for label in row.find_elements(By.CSS_SELECTOR, 'td > label'):
        label.click()

        #copy button
        copyButton = driver.find_element(By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/div/div[2]/a[2]')
        copyButton.send_keys(Keys.CONTROL + Keys.ENTER)
        log.info('Copying...')
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
        log.info('Finished')

        #close & switch tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

#print elapsed time
end = time.time()
elapsed = end - start
log.info('All ' + str(count) + ' Tasks Completed in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()