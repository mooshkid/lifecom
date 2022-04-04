from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd
import time
import os
import sys
import logging

#logging config
path = os.getcwd()
logPath = os.path.join(path, "logs/engage_life.log")

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

#excel path
excelPath = os.path.join(path, 'Engage/engage_life.xlsx')
#dataframes
df = pd.read_excel(excelPath)
#'job' column list
job_list = df['job'].tolist()

#chrome options
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 8')
driver = webdriver.Chrome(options=options)

#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://en-gage.net/company/job/?PK=D2B206")

#start time
start = time.time()
#loop counter
count = 1

#start loop
for i in job_list:
    log.info('Starting(' + str(count) + '): ' + i)

    #copy button
    copyButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="md_pageTitle"]/a[2]')))
    copyButton.click()
    #search box
    searchBox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="listParamFormEngage"]/div/input')))
    searchBox.clear()
    searchBox.send_keys(i)
    time.sleep(1)
    searchEnter = driver.find_element(By.XPATH, '//*[@id="listParamFormEngage"]/div/button')
    searchEnter.click()

    #copy post
    time.sleep(2)
    copyButton = driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/a')
    copyButton.click()

    #overtime (only for fulltime)
    try:
        overtimeLabel = driver.find_element(By.XPATH, '//*[@id="jobMakeForm"]/div[1]/div[2]/dl/dd[6]/dl/dd[9]/div/div/div[1]/label')
        overtimeLabel.click()
    except ElementNotInteractableException:
        pass

    #vacation
    vacationSelect = driver.find_element(By.XPATH, '//*[@id="holiday_system"]')
    vacationSelect.click()
    vacationSelect.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)

    #required Checkboxes
    time.sleep(1)
    reqHoliday = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[2]/dl/dd/div/div/div/label')))
    reqHoliday.click()
    reqWage = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[3]/dl/dd[1]/div/div/div/label')
    reqWage.click()
    reqWrite = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[3]/dl/dd[2]/div/div/div/label')
    reqWrite.click()
    reqHours = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[4]/dl/dd/div/div/div/label')
    reqHours.click()
    reqWelfare = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[5]/dl/dd/div/div/div/label')
    reqWelfare.click()
    reqCopyright = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/dl/dd[1]/div/div/div/label')
    reqCopyright.click()
    reqAgency = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/dl/dd[2]/div/div/div/label')
    reqAgency.click()

    #confirm changes
    confirmChanges = driver.find_element(By.XPATH, '//*[@id="jobMakeFormButton"]/a')
    confirmChanges.click()
    #next
    nextButton = driver.find_element(By.XPATH, '//*[@id="jobMakeFormButton"]/div/a[2]')
    nextButton.click()

    #skip premium
    noPremium = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobFormBase"]/div[2]/a')))
    noPremium.click()

    log.info('Copy Created')
    
    #close popup
    #//*[@id="karte-9843225"]/div[2]/div/div/section/button

    #START CLOSE
    #published filter
    published = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')
    published.click()
    #search for post again
    searchBoxDelete = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[3]/div/span/input')
    searchBoxDelete.clear()
    searchBoxDelete.send_keys(i)
    #filter
    filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a')
    filterButton.click()

    #unpublish
    unpublish = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/tbody/tr[2]/td[6]/span/select/option[2]')
    unpublish.click()

    #select reason
    reason = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[1]/dl/dd/div/div[6]/label')
    reason.click()
    #click send
    send = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[2]/a[2]')
    send.click()

    log.info('Closed Original Post')
    count += 1

#elapsed time
end = time.time()
elapsed = end - start
log.info('All ' + str(count) + ' Tasks Completed Successfully in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()