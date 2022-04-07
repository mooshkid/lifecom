from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import logging

#logging config
logging.basicConfig(
    level=logging.INFO,
    format=u'%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("C:\\Users\\yamanaka\\Documents\\VSCode\\lifecom\\Indeed\\logs.log", encoding='utf8'),
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
options.add_argument('--profile-directory=Profile 9')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

#launch URL
driver.get("https://employers.indeed.com/j#cdjobs") #tab for copying
driver.execute_script("window.open('https://employers.indeed.com/j#cdjobs');") #tab for closing
driver.switch_to.window(driver.window_handles[1])
time.sleep(6)

#loop counter
count = 0
#start timer
start = time.time()
#create empty list
theList = []

#find number of open jobs
rows = driver.find_elements(By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/table/tbody/tr')
jobCount = len(rows)
log.info(str(jobCount) + ' Open Job Listings Found')
#print list of all open jobs
for row in rows:
    for ahref in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a'):
        jobTitle = ahref.text
        theList.append(jobTitle)
log.info(theList)

#CLOSE all open jobs
log.info('Closing All Jobs')
selectAll = driver.find_element(By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/table/thead/tr/th[1]/label').click()
changeStatusButton = driver.find_element(By.XPATH, '//*[@id="BulkUpdateStatusMenuButton"]').click()
closeAll = driver.find_element(By.XPATH, '//*[@id="option-2--menu--2"]')    #  //*[@id="option-2--menu--6"]
closeAll.click()
time.sleep(1)

driver.switch_to.alert.accept() #driver.switch_to.alert.dismiss()
log.info('Closed All Jobs')
time.sleep(1)

#close & switch tab
driver.close()
driver.switch_to.window(driver.window_handles[0])

#START Copying
for row in rows:
    for ahref in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a'):
        jobTitle = ahref.text
        count += 1
        log.info('Starting(' + str(count) + '): ' + jobTitle)
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
        log.info('Finished.')

        #close & switch tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

#print elapsed time
end = time.time()
elapsed = end - start
log.info('All ' + str(count) + ' Jobs Successfully Updated in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()