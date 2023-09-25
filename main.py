from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

class Main(webdriver.Edge):
    def __init__(self, teardown=False):
        super(Main, self).__init__(options=options)
        self.teardown = teardown
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self):
        if self.teardown:
            self.quit()

    def lauch_web(self, url):
        self.get(url)

    def login(self, username, password):
        usernameField = self.find_element(By.NAME, "j_username")
        passwordField = self.find_element(By.NAME, "j_password")

        usernameField.send_keys(username)
        passwordField.send_keys(password)

        submitBtn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submitBtn.click()

        print("Login Successful!")

    def openRootPage(self):
        print("I ran")
        self.get("https://erp.meu.edu.in/stu_studentTest.htm")
        print("But, I ran")
        # academicFunctionsBtn = self.find_element(By.CSS_SELECTOR, 'a[pid="20009"]')
        # academicFunctionsBtn.click()

        # self.implicitly_wait(1000)

        # onlineAssessmentBtn = self.find_element(By.CLASS_NAME, 'a[pid="21893"]')
        # onlineAssessmentBtn.click()
