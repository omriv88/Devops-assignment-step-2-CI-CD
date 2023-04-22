from selenium import webdriver
from selenium.webdriver.common.by import By



my_driver = webdriver.Chrome(executable_path= r'C:\webdrivers\107\chromedriver.exe')
my_driver.get('http://ngixn_dl:8080/')


title = my_driver.title

expected_title = "omriv is doing the assignment.!"
if title == expected_title:
    print("Good - the title is 'omriv is doing the assignment'")
else:
    print("X")


my_driver.close()
