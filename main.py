from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

class Main(webdriver.Edge):
    def __init__(self):
        super(Main, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self):
        self.quit()

    def lauch_web(self, url):
        print("Opening Website")
        self.get(url)

    def login(self, username, password):
        print("Trying to Log-In")
        usernameField = self.find_element(By.NAME, "j_username")
        passwordField = self.find_element(By.NAME, "j_password")

        usernameField.send_keys(username)
        passwordField.send_keys(password)

        submitBtn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submitBtn.click()

        print("Login Successful!")

    def openRootPage(self):
        self.get("https://erp.meu.edu.in/stu_studentTest.htm")

    def getTests(self):
        print("Getting Tests")
        
        container = self.find_element(By.ID, "availableTestDiv")
        testsData = container.find_elements(By.TAG_NAME, "tr")
        self.testsData = testsData

        print("Got the Data of test.")

    def getSpecificTest(self, testNumber):
        test = self.testsData[testNumber]
        testCols = test.find_elements(By.TAG_NAME, "td")

        print("Test Name:", testCols[0].text)
        print("Subject:", testCols[1].text)

    # def 