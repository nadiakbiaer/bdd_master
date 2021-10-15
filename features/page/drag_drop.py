

import allure
from Browser import Browser
from selenium.webdriver import ActionChains

objectTodrag = 'draggable'
objectTodrop = 'droppable'



class drag_drop(Browser):

    def url(self, link):
        self.driver.get(link)


    def drag(self):

        source1 = self.driver.find_element_by_id(objectTodrag)
        target1 = self.driver.find_element_by_id(objectTodrop)
        actions1 = ActionChains(self.driver)
        actions1.drag_and_drop(source1, target1).perform()

    def slider(self):
        slider =self.driver.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]')
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(131, 0).release().perform()

    def affichageSlider(self):
        slider= self.driver.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/span[1]').text
        return (slider)

    def affichageDrop(self):
        msg = self.driver.find_element_by_id("dropText").text
        return(msg)

