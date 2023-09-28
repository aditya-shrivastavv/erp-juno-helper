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

    def openTestsPage(self):
        acedemicFnsBtn = self.find_element(By.CSS_SELECTOR, 'a[pid="20009"]')
        acedemicFnsBtn.click()

        onlineAssessmentBtn = self.find_element(
            By.CSS_SELECTOR, 'a[href="stu_studentTest.htm"]'
        )

        wait = WebDriverWait(self, timeout=5)
        wait.until(lambda pause: onlineAssessmentBtn.is_displayed())

        onlineAssessmentBtn.click()

    def getTests(self):
        print("Getting Tests")

        container = self.find_element(By.ID, "availableTestDiv")
        self.testsData = container.find_elements(By.TAG_NAME, "tr")

        print("Got the Data of test.")

    def getSpecificTest(self, testNumber):
        self.targetTest = self.testsData[testNumber]
        self.targetTestCols = self.targetTest.find_elements(By.TAG_NAME, "td")

        print("Test Name:", self.targetTestCols[0].text)
        print("Subject:", self.targetTestCols[1].text)

    def startTest(self):
        startBtn = self.targetTestCols[-1].find_element(By.TAG_NAME, "button")
        startBtn.click()

        bigStartBtn = self.find_element(By.ID, "idStartTestImg")
        bigStartBtn.click()

        try:
            # Password filled here
            pass
        except ():
            print("Either no Password needed or Unknown execption")


    def collectQuestionsAndOptions(self):
        quesNumTable = self.find_element(By.ID, "questionImg")
        questionsChips = quesNumTable.find_elements(By.TAG_NAME, "span")

        for chip in questionsChips:
            chip.click()

            questionBox = self.find_element(By.ID, "questionDiv")
            question = questionBox.find_element(By.ID, "questionTd")

            optionsBox = questionBox.find_element(By.CLASS_NAME, "opDivSelectionBox")
            options = optionsBox.find_elements(By.TAG_NAME, "span")

            with open("result.txt", "a") as file:
                file.write("- - - x - - - x - - - x - - - x - - - x - - - x - - -\n")
                file.write(f"{question.text}\n\n")
                file.write("Options are:")
                for option in options:
                    file.write(f"{option.text}\n")
