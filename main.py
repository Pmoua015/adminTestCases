import unittest

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import time


class AdminTestingCases(unittest.TestCase):

    def setUp(self):
        s = Service("/Users/yorkmac003/PycharmProjects/adminTestCases/venv/bin/chromedriver 2.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://yorkdevtraining.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, "mat-button-wrapper").click()
        Email = ""
        Password = ""
        self.driver.find_element("id", "mat-input-0").send_keys(Email)
        self.driver.find_element("id", "mat-input-1").send_keys(Password)

        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "mat-card"))
            )

            divs = main.find_elements(By.TAG_NAME, "button")
            for button in divs:
                button.find_element(By.CLASS_NAME, "mat-button-wrapper").click()

            self.driver.find_element(By.XPATH, "//span[@class='mat-button-wrapper' and text()='User Lookup']").click()

            time.sleep(5)

            sel = self.driver.find_element(By.TAG_NAME, "mat-form-field")
            sel.find_element(By.XPATH,
                             "/html/body/app-root/app-user-table/div/div[1]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span").click()
            self.driver.find_element(By.ID, "mat-select-0-panel")
            self.driver.find_element(By.ID, "mat-option-21").click()

            time.sleep(3)

            self.driver.find_element(By.ID, "mat-input-7").send_keys("bob1@")

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )

            element.find_element(By.CLASS_NAME, "mat-button-wrapper").click()

            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[1])

            self.driver.find_element(By.ID, "mat-expansion-panel-header-204").click()

            self.driver.find_element(By.ID, "mat-expansion-panel-header-202").click()

        finally:
            time.sleep(5)

    # 'Learn Javascript with HTML' testing
    def test_valid(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("helloWor9")
        div.find_element(By.ID, "fname").send_keys("hello")
        div.find_element(By.ID, "lname").send_keys("world")
        div.find_element(By.ID, "bday").send_keys("01/01/2000")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "")

    def test_no_number_included(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("hellowor")
        div.find_element(By.ID, "fname").send_keys("hello")
        div.find_element(By.ID, "lname").send_keys("world")
        div.find_element(By.ID, "bday").send_keys("01/01/2000")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "Invalid UserID")

    def test_more_than_12_characters(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("helloWorldddd9")
        div.find_element(By.ID, "fname").send_keys("hello")
        div.find_element(By.ID, "lname").send_keys("world")
        div.find_element(By.ID, "bday").send_keys("01/01/2000")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "Invalid UserID")

    def test_all_lower_case_letters(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("helloworld9")
        div.find_element(By.ID, "fname").send_keys("hello")
        div.find_element(By.ID, "lname").send_keys("world")
        div.find_element(By.ID, "bday").send_keys("01/01/2000")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "Invalid UserID")

    def test_less_than_8_characters(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("helloW9")
        div.find_element(By.ID, "fname").send_keys("hello")
        div.find_element(By.ID, "lname").send_keys("world")
        div.find_element(By.ID, "bday").send_keys("01/01/2000")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "Invalid UserID")

    def test_individual_enters_nothing(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[3]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "div")
        div.find_element(By.ID, "user_id").send_keys("")
        div.find_element(By.ID, "fname").send_keys("")
        div.find_element(By.ID, "lname").send_keys("")
        div.find_element(By.ID, "bday").send_keys("")
        div.find_element(By.XPATH, "//input[@type='button']").click()

        output = div.find_element(By.ID, "output")
        print(output.text)

        self.assertEqual(output.text, "Invalid UserID\nInvalid fname\nInvalid lname\nInvalid Birth Day")

    # this is HTML testing
    def test_My_First_HTML_Page(self):
        iframe = self.driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-user-lookup/mat-card/mat-card[5]/mat-card-content/mat-accordion/mat-expansion-panel[1]/div/div/div/app-html-ide/div[2]/iframe")

        self.driver.switch_to.frame(iframe)
        div = self.driver.find_element(By.TAG_NAME, "body")

        # verifies the heading includes "My First HTML Page"
        text = div.find_element(By.TAG_NAME, "h1")
        print(text.text)
        self.assertEqual(text.text, "My First HTML Page")

        # verifies the paragraph has at least 30 words
        paragraph = div.find_element(By.TAG_NAME, "p")
        print(len(paragraph.text.split()))
        self.assertTrue(len(paragraph.text.split()) >= 30)

        # verifies the img height is 300 & width is 200
        img = div.find_element(By.XPATH, "/html/body/img[1]")
        print(img.size)
        self.assertTrue(img.size == {'height': 300, 'width': 200})
        alt = img.get_attribute('alt')
        print(alt)
        actual_text = alt
        self.assertTrue(alt == actual_text)

        img = div.find_element(By.XPATH, "/html/body/img[2]")
        print(img.size)
        self.assertTrue(img.size == {'height': 300, 'width': 200})
        alt = img.get_attribute('alt')
        print(alt)
        actual_text = alt
        self.assertTrue(alt == actual_text)

        # checks to see if links work
        div.find_element(By.XPATH, "/html/body/header/a[1]").click()
        card_link = div.find_element(By.XPATH, "/html/body/header/a[1]").get_attribute('href')
        request_response = requests.head(card_link)
        status_code = request_response.status_code
        if status_code == 200:
            print("URL is valid")
        else:
            print("URL is invalid")
        self.assertTrue(status_code == 200)

        div.find_element(By.XPATH, "/html/body/header/a[2]").click()
        card_link = div.find_element(By.XPATH, "/html/body/header/a[1]").get_attribute('href')
        request_response = requests.head(card_link)
        status_code = request_response.status_code
        if status_code == 200:
            print("URL is valid")
        else:
            print("URL is invalid")
        self.assertTrue(status_code == 200)

        div.find_element(By.XPATH, "/html/body/header/a[3]").click()
        card_link = div.find_element(By.XPATH, "/html/body/header/a[1]").get_attribute('href')
        request_response = requests.head(card_link)
        status_code = request_response.status_code
        if status_code == 200:
            print("URL is valid")
        else:
            print("URL is invalid")
        self.assertTrue(status_code == 200)

        div.find_element(By.XPATH, "/html/body/header/a[4]").click()
        card_link = div.find_element(By.XPATH, "/html/body/header/a[1]").get_attribute('href')
        request_response = requests.head(card_link)
        status_code = request_response.status_code
        if status_code == 200:
            print("URL is valid")
        else:
            print("URL is invalid")
        self.assertTrue(status_code == 200)

        time.sleep(10)

        # prints out what is written in the table
        table = div.find_element(By.XPATH, "/html/body/table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            row.find_elements(By.TAG_NAME, "td")
        print(row.text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
