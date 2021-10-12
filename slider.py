
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://qavbox.github.io/demo/dragndrop/")
driver.maximize_window()
slider = driver.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]')

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(131, 0).release().perform()
msg=driver.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/span[1]').text
print("msg",msg)