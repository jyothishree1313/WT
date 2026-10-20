from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

driver.get("http://localhost:3000")
#1 Interface
assert "Inventory Sys" in driver.page_source

driver.find_element(By.XPATH,"//input[@ng-model='id']")
driver.find_element(By.XPATH,"//input[@ng-model='name']")
print("Interface test :PASSED")

#Usability
driver.find_element(By.XPATH,"//input[@ng-model='id']").send_keys("102")
driver.find_element(By.XPATH,"//input[@ng-model='name']").send_keys("kinderjoy")
driver.find_element(By.XPATH,"//input[@ng-model='quantity']").send_keys("3")
driver.find_element(By.XPATH,"//input[@ng-model='price']").send_keys("300")

driver.find_element(By.XPATH,"//button[text()='Add']").click()

wait.until(lambda d:"kinderjoy" in d.find_element(By.TAG_NAME,"table").text)
print("Usability:PASSED")


#functionality
row=driver.find_element(By.XPATH,"//tr[td[contains(text(),'kinderjoy')]]")
driver.find_element(By.XPATH,"//button[text()='Update']").click()

name=driver.find_element(By.XPATH,"//input[@ng-model='name']")
name.clear()
name.send_keys("choco")
driver.find_element(By.XPATH,"//button[text()='Add']").click()

wait.until(lambda d: "choco" in d.find_element(By.TAG_NAME,"table").text)
print("Functionality Update :PASSED")

row=driver.find_element(By.XPATH,"//tr[td[contains(text(),'choco')]]")
row.find_element(By.XPATH,".//button[text()='Delete']").click()

wait.until( lambda d: 'choco' not in d.find_element(By.TAG_NAME,"table").text)
print("Functionality delete: Successfull!")


driver.quit()