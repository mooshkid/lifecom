### NEED MAJOR REVISION ###
### Website has been revised
### 5/30/2022 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd
import time

#dataframes
df = pd.read_excel('Engage/engage_little.xlsx')
#'job' column list
job_list = df['job'].tolist()

#chrome options
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\yamanaka\\AppData\\Local\\Google\\Chrome\\User Data')  #change path to your chrome profile (chrome://version/)
options.add_argument('--profile-directory=Profile 9')   #change profile # as needed
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

#launch URL
driver.get("https://en-gage.net/company/job/?PK=5AEE24")

#start time
start = time.time()
#loop counter
count = 1

#filter by published
publishedFilter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')))
publishedFilter.click()
#click filter button
filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a').click()


#start loop
for i in job_list:
    print('Starting(' + str(count) + '): ' + i)

    #copy button
    copyButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="md_pageTitle"]/a[2]')))
    copyButton.click()
    #search box
    time.sleep(2)
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

    print('Copy Created')
    count += 1
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
tt = end - start
print('Completed in: ' + str(tt) + ' seconds')

driver.close()