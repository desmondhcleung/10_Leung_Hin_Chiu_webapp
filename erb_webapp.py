from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
url = "https://www.directory.gov.hk/basic_service2.jsp?desc=&ou=&name=E&lang=eng"
driver.get(url)
driver.maximize_window()

table_body = driver.find_element(By.TAG_NAME, "tbody")
table_rows = table_body.find_elements(By.TAG_NAME, "tr")

with open("gov_dept_tel.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for row in table_rows:
        table_data = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        for data in table_data:
            row_data.append(data.text)
        writer.writerow(row_data)

driver.quit()
