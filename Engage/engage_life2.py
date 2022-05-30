#### NO EXCEL VERSION ####
## 5/12/2022

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time

#chrome options (change path to your chrome profile!!! chrome://version/)
options = webdriver.ChromeOptions()
#options.add_argument('--user-data-dir=C:\\Users\\kokoku\\AppData\\Local\\Google\\Chrome\\User Data')
#options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 8')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

#launch URL
driver.get("https://en-gage.net/company/job/?PK=D2B206")

#start time
start = time.time()
#loop counter
count = 0
#create an empty list
theList = []

#filter by published
publishedFilter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')))
publishedFilter.click()
#click filter button
filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a').click()
#sort by date ascending
sortDate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobIndexTable"]/table/thead/tr/th[3]/a')))
sortDate.click()

#CREATE THE LIST
time.sleep(2)
table = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table')
for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
    for aTag in row.find_elements(By.CSS_SELECTOR, 'td:nth-child(1) > div > a'):
        jobTitle = aTag.text
        theList.append(jobTitle)

print(theList)
print(str(len(theList)) + ' Open Jobs Found')


#START LOOP
for i in theList:
    #copy button
    copyButton = driver.find_element(By.XPATH, '//*[@id="md_pageTitle"]/a[2]')
    copyButton.click()

    count += 1
    print('Starting(' +str(count) + '): ' + i)

    #search box
    searchBox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="listParamFormEngage"]/div/input')))
    searchBox.clear()
    searchBox.send_keys(i)
    time.sleep(1)
    searchEnter = driver.find_element(By.XPATH, '//*[@id="listParamFormEngage"]/div/button')
    searchEnter.click()
    time.sleep(2)

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
    time.sleep(2)
    nextButton = driver.find_element(By.XPATH, '//*[@id="jobMakeFormButton"]/div/a[2]')
    nextButton.click()

    #skip premium
    noPremium = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobFormBase"]/div[2]/a')))
    noPremium.click()

    print('Copy Created')

    #close popup
    #//*[@id="karte-9843225"]/div[2]/div/div/section/button


    #START JOB CLOSE
    #search for post again
    searchBoxDelete = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[3]/div/span/input')
    searchBoxDelete.clear()
    searchBoxDelete.send_keys(i)
    #published filter
    published = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')
    published.click()
    #filter
    filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a')
    filterButton.click()

    #unpublish
    time.sleep(2)
    unpublish = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/tbody/tr[2]/td[6]/span/select/option[2]')
    unpublish.click()

    #select reason
    reason = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[1]/dl/dd/div/div[6]/label')
    reason.click()
    #click send
    send = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[2]/a[2]')
    send.click()

    print('Closed Original Post')

#elapsed time
end = time.time()
elapsed = end - start
print('All ' + str(count) + ' Tasks Completed Successfully in: ' + time.strftime('%H:%M:%S', time.gmtime(elapsed)))

driver.close()