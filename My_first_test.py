# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Pamono(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pamono(self):
        driver = self.driver
        driver.get("http://pss.staging.pamono.com/")
        driver.find_element_by_id("orderList").click()
        driver.find_element_by_link_text("it's a place for logo").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='kg'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assigned'])[1]/following::div[1]").click()
        driver.find_element_by_id("msgpost").click()
        driver.find_element_by_id("msgpost").clear()
        driver.find_element_by_id("msgpost").send_keys("Hello!")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Activities Log'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='all'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='kg'])[1]/following::div[2]").click()
        driver.find_element_by_id("msgpost").click()
        driver.find_element_by_id("msgpost").clear()
        driver.find_element_by_id("msgpost").send_keys("Good morning!")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Less than a minute ago, MoveAndParcel'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Less than a minute ago, MoveAndParcel'])[2]/following::button[1]").click()
        driver.find_element_by_name("shipping-price").click()
        driver.find_element_by_name("shipping-price").clear()
        driver.find_element_by_name("shipping-price").send_keys(u"10€")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Less than a minute ago, MoveAndParcel'])[2]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Shipping Price'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pick-up date'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sun'])[1]/following::button[19]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Drop-off date'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sun'])[1]/following::button[31]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Less than a minute ago, MoveAndParcel'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
