from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time
import sys
import logging

#logging config
path = os.getcwd()
logPath = os.path.join(path, "logs/indeed_little.log")
#logPath = os.path.expanduser('~/Documents/Python/Lifecom/Logs/indeed_little.log')

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
options.add_argument('--profile-directory=Profile 9')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

#launch URL
driver.get("https://employers.indeed.com/j#cdjobs") 

#loop counter
count = 0
#start timer
start = time.time()

#sort date by asc
sortDate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/table/thead/tr/th[4]/button'))).click()
time.sleep(2)

#find number of open jobs
rows = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cdjobstab"]/div[3]/div/table/tbody/tr')))
jobCount = len(rows)
log.info(str(jobCount) + ' Open Job Listings Found')

#start loop
for row in rows:
    for aTag in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a'):
        count +=1
        log.info('Starting(' + str(count) + '): ' + aTag.text)

    #open post in new tab
    aTag.send_keys(Keys.CONTROL + Keys.ENTER)
    #switch to tab1
    driver.switch_to.window(driver.window_handles[1])

    #status button
    time.sleep(4)
    statusButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-0-toggle-button"]')))
    statusButton.click()
    #close job
    closeJob = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-0-item-2"]')))
    closeJob.click()
    #reason
    reasonOne = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="billingOrTechnicalIssue"]/ancestor::label')))
    reasonOne.click()
    #click next
    clickNext = driver.find_element(By.CLASS_NAME, 'continue-btn').click()
    #reason 2
    reasonTwo = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.question-content > ul > li:nth-child(5)')))
    reasonTwo.click()
    #click confirm
    clickConfirm = driver.find_element(By.CSS_SELECTOR, 'div.button-and-link-container > button:nth-child(2)').click()
    log.info('Closed')
    time.sleep(1)

    #close & switch tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

    # Duplicate loop    
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

    ##### NEW PART #######
    #next button 1
    nextButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[5]/div/div/div/div[2]/div[2]/button')))
    nextButton.click()
    #next again 2
    hireOne = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form > div > div > div:nth-child(3) > div > div:nth-child(1) select > option:nth-child(2)'))).click()
    hireTwo = driver.find_element(By.CSS_SELECTOR, 'form > div > div > div:nth-child(3) > div > div:nth-child(2) select > option:nth-child(4)').click()
    nextButton2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[5]/div/div/div/div[2]/div[2]/button')))
    nextButton2.click()
    #next again 3
    nextButton3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[5]/div/div/div/div[2]/div[2]/button')))
    nextButton3.click()
    #next again 4
    nextButton4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[5]/div/div/div/div[2]/div[2]/button')))
    nextButton4.click()
    #next again 5
    nextButton5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[5]/div/div/div/div[2]/div[2]/button')))
    nextButton5.click()
    #next again 6
    nextButton6 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[4]/div/div/div/div[2]/div[2]/button')))
    nextButton6.click()

    try:
        #next again 7
        time.sleep(2)
        nextButton7 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/form/div/div[4]/div/div/div/div[2]/div[2]/button')))
        nextButton7.click()
    except TimeoutException:
        pass

    #unpaidOption 8
    unpaidOption = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/div[3]/main/div/div/div[3]/button[1]')))
    unpaidOption.click()
    log.info('Finished')
    time.sleep(1)

    #close & switch tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

#print elapsed time
end = time.time()
elapsed = end - start
log.info('All ' + str(count) + ' Jobs Successfully Updated in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()