
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://localhost:3000")

# 1. INTERFACE TESTING
assert "Inventory System" in driver.page_source
driver.find_element(By.XPATH, "//input[@ng-model='id']")
driver.find_element(By.XPATH, "//input[@ng-model='name']")

print("Interface Testing: Passed")

# 2. USABILITY TESTING
driver.find_element(By.XPATH, "//input[@ng-model='id']").send_keys("101")
driver.find_element(By.XPATH, "//input[@ng-model='name']").send_keys("Pen")
driver.find_element(By.XPATH, "//input[@ng-model='quantity']").send_keys("10")
driver.find_element(By.XPATH, "//input[@ng-model='price']").send_keys("5")

driver.find_element(By.XPATH, "//button[text()='Add']").click()

wait.until(lambda d: "Pen" in d.find_element(By.TAG_NAME, "table").text)

print("Usability Testing: Passed")

# 3. FUNCTIONAL TESTING - UPDATE
row = driver.find_element(By.XPATH, "//tr[td[contains(text(),'Pen')]]")
row.find_element(By.XPATH, ".//button[text()='Update']").click()

name = driver.find_element(By.XPATH, "//input[@ng-model='name']")
name.clear()
name.send_keys("Pencil")

driver.find_element(By.XPATH, "//button[text()='Add']").click()

wait.until(lambda d: "Pencil" in d.find_element(By.TAG_NAME, "table").text)

print("Update Testing: Passed")

# 4. FUNCTIONAL TESTING - DELETE
row = driver.find_element(By.XPATH, "//tr[td[contains(text(),'Pencil')]]")
row.find_element(By.XPATH, ".//button[text()='Delete']").click()

wait.until(lambda d: "Pencil" not in d.find_element(By.TAG_NAME, "table").text)

print("Delete Testing: Passed")

driver.quit()
