import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Parse import Parse

# Get chorome Driver
driver = webdriver.Chrome('/Users/aldo/PycharmProjects/scriptGM/chromedriver')

# Go to goldmine
driver.get('https://www.goldmine.utep.edu/prod/owa/bwckschd.p_disp_dyn_sched')
time.sleep(0.5)

# Go to courses page of goldmine
driver.find_element(By.XPATH,'/html/body/div[4]/form/table/tbody/tr/td/select/option[2]').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[4]/form/input[2]').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[4]/form/input[12]').click()

# Get correct HTML
GMcourses=driver.find_element(By.CLASS_NAME,'datadisplaytable')
print('DONE get HTML')

#Write HTML no tags to txt
file = open('/Users/aldo/PycharmProjects/scriptGM/HTML_no-tags.txt','w')
print('DONE remove HTML tags')
file.write(GMcourses.text)
print('DONE HTML no tags txt file')
file.close()

#Turn HTML TO JSON strings and put on txt file
file = open('/Users/aldo/PycharmProjects/scriptGM/HTML_no-tags.txt','r')
HTML_no_tags = file.readlines()
print('DONE reading HTML no tags')
parsed= Parse.Parse(HTML_no_tags)
file.close()
print('DONE PARSE HTML no tags to JSON')
file = open('/Users/aldo/PycharmProjects/scriptGM/Parsed.txt','w')
file.write(parsed)
print('DONE JSON txt file')

# END
driver.close()