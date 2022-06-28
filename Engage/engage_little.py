### Updated 6/14/2022 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys
import logging


# change cwd to the script directory 
os.chdir(os.path.dirname(__file__))
path = os.getcwd()

# log file path
logPath = os.path.join(path, "../Logs/indeed_little.log")
# logging config 
logging.basicConfig(
    level=logging.INFO,
    format=u'%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(logPath, encoding='utf8', mode='a'),
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


# chrome options 
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\kokoku\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 2')
# options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--profile-directory=Profile 9')
# options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

# launch URL 
driver.get("https://en-gage.net/company/job/?PK=5AEE24")

# counter 
count = 0
#start time
start = time.time()


# close top message bar 
try:
    driver.find_element(By.CLASS_NAME, 'applicantAlert__close').click()
except ElementNotInteractableException:
    pass

# filter by published
publishedFilter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')))
publishedFilter.click()
# click filter button 
filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a').click()
# total published posts 
totalPosts = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobIndexTable"]/div[1]/div[1]/em'))).text
log.info('There are ' + totalPosts + ' Published Posts')


### Start the loop ###
for i in range(int(totalPosts)):
    count += 1
    
    # filter by published
    publishedFilter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')))
    publishedFilter.click()
    # click filter button 
    filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a').click()
    # sort by date asc 
    time.sleep(2)
    sortDate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobIndexTable"]/table/thead/tr/th[3]/a'))).click()

    # find the elements
    time.sleep(2)
    table = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobIndexTable"]/table/tbody')))
    rows = table.find_element(By.CSS_SELECTOR, 'tr')
    # print title 
    title = rows.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > div > a')
    log.info('Starting(' + str(count) + '): ' + title.text)


    ### CLOSE ORIGINAL POST ###
    # change to closed status 
    closePost = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/tbody/tr[1]/td[6]/span/select/option[2]').click()
    # select reason
    time.sleep(1)
    reason = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[1]/dl/dd/div/div[6]/label').click()
    # click send 
    send = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[2]/a[2]').click()
    log.info('Closed Original Post')


    ### COPY ORIGINAL POST ###
    time.sleep(2)
    log.info('Creating Copy')
    # click copy 
    WebDriverWait(rows, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td:nth-of-type(1) > a:nth-of-type(2)'))).click()

    #overtime (only for fulltime)
    try:
        overtimeLabel = driver.find_element(By.XPATH, '//*[@id="jobMakeForm"]/div[1]/div[2]/dl/dd[6]/dl/dd[9]/div/div/div[1]/label')
        overtimeLabel.click()
    except ElementNotInteractableException:
        pass

    #vacation
    vacationSelect = driver.find_element(By.XPATH, '//*[@id="holiday_system"]/option[4]')
    vacationSelect.click()

    #required Checkboxes
    try:
        time.sleep(1)
        reqHoliday = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[2]/div[2]/dl/dd/div[2]/dl/dd/div/div/div/label')
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
    except NoSuchElementException:
        pass

    #confirm changes
    confirmChanges = driver.find_element(By.XPATH, '//*[@id="jobMakeFormButton"]/a')
    confirmChanges.click()
    #next
    time.sleep(2)
    nextButton = driver.find_element(By.XPATH, '//*[@id="jobMakeFormButton"]/div/a[2]')
    nextButton.click()
    #skip premium
    noPremium = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobFormBase"]/div[2]/a')))
    noPremium.click()

    log.info('Copy Created')

#elapsed time
end = time.time()
elapsed = end - start
log.info('All ' + str(count) + ' Tasks Completed Successfully in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()