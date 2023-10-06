from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

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

    def startTest(self, passwordData=[False]):
        startBtn = self.targetTestCols[-1].find_element(By.TAG_NAME, "button")
        startBtn.click()

        if passwordData[0]:
            passwordField = self.find_element(By.ID, "txtKeyVerification")
            passwordField.send_keys(passwordData[1])

            verifyBtn = self.find_element(By.ID, "btnSubmitKeyVerification")
            verifyBtn.click()

        time.sleep(1)

        bigStartBtn = self.find_element(By.ID, "idStartTestImg")
        wait = WebDriverWait(self, timeout=5)
        
        wait.until(lambda pause: bigStartBtn.is_displayed())
        bigStartBtn.click()


    def collectQuestionsAndOptions(self):
        quesNumTable = self.find_element(By.ID, "questionImg")
        questionsChips = quesNumTable.find_elements(By.TAG_NAME, "span")

        for chip in questionsChips:
            chip.click()

            parentContainer = self.find_element(By.ID, "questionDiv")
            
            questionContainer = self.find_element(By.ID, "questionTd")
            questionNumber = questionContainer.find_element(By.TAG_NAME, "span")
            question = questionContainer.find_element(By.TAG_NAME, "b")

            optionBoxes = parentContainer.find_elements(By.CLASS_NAME, "opDivSelectionBox")

            with open("result.txt", "a", encoding='utf-8') as file:
                file.write("\n- - - x - - - x - - - x - - - x - - - x - - - x - - -\n\n")
                file.write(f"{questionNumber.text}\n")
                file.write(f"{question.text}\n\n")
                file.write("Options are:\n\n")
                for optionBox in optionBoxes:
                    option = optionBox.find_element(By.TAG_NAME, "label")
                    file.write(f"{option.text}\n")
