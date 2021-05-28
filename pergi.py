from selenium import webdriver
# from selenium import Firefox
import time
import datetime
# from selenium import chrome

web = webdriver.Firefox()

web.get('https://docs.google.com/forms/d/16GCdM7KI57n6laASeKXC81L9BSnFZjchpx2PxUh3pVY?hl=en')

time.sleep(2)

month = datetime.date.today()
mtd = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
mtd.send_keys(month.month)

dtd = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/input')
dtd.send_keys(month.day)

ytd = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[5]/div/div[2]/div[1]/div/div[1]/input')
ytd.send_keys(month.year)

name = "ANDREAS YOZEF"
nameb = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
nameb.send_keys(name)

radio1 = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]')
radio1.click()

radio2 = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[7]/label/div/div[1]/div/div[3]')
radio2.click()



dayl = datetime.date.today()
weekl = dayl.weekday()
mapel = ""
if weekl == 0:
    mapel= "bahasa indonesia"
if weekl == 1:
    mapel= "pemrograman web"
if weekl == 2:
    mapel= "basis data"
if weekl == 3:
    mapel= "pemrograman web"
if weekl == 4:
    mapel= "PAI"



name = mapel
nameb = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
nameb.send_keys(name)


submit = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div/div')
submit.click()


ss=datetime.datetime.now()
conf = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(conf.text)
if((conf.text)== "Your response has been recorded."):
    print("absensi berhasil pergi pada ")
    print(ss)
else:
    print("gagal")


time.sleep(3)
web.quit()

