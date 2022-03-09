from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#dataframes
df = pd.read_excel('python\selenium\kosuke\engage.xlsx')
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
driver.get("https://en-gage.net/company/job/?PK=5AEE24")

#start time
start = time.time()
#loop counter
count = 1

    
#status
published = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[2]/div[2]/span/select/option[2]')
published.click()
#filter
filterButton = driver.find_element(By.XPATH, '//*[@id="conditionForm"]/ul/li[4]/div/a')
filterButton.click()

#sort date by asc
sortDate = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/thead/tr/th[3]/a')
sortDate.click()
time.sleep(2)

#start loop
for i in job_list:

    #job title
    jobTitle = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/tbody/tr[' + str(count) + ']/td[1]/div[1]/a').text
    print('Closing(' + str(count) + '): ' + jobTitle)

    #unpublish
    time.sleep(2)
    unpublish = driver.find_element(By.XPATH, '//*[@id="jobIndexTable"]/table/tbody/tr[' + str(count) + ']/td[6]/span/select/option[2]')
    unpublish.click()

    #select reason
    reason = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[1]/dl/dd/div/div[6]/label')
    reason.click()
    #click send
    send = driver.find_element(By.XPATH, '//*[@id="stopModalForm"]/div/div/div[2]/a[2]')
    send.click()


    print('Finished')
    count += 1

#elapsed time
end = time.time()
tt = end - start
print('Completed in: ' + str(tt) + ' seconds')

driver.close()