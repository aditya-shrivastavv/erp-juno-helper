from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)


def printX(color="white", text=""):
    code = "\033[1;37;40m"
    if color == "red":
        code = "\033[1;31;40m"
    elif color == "green":
        code = "\033[1;32;40m"
    elif color == "yellow":
        code = "\033[1;33;40m"
    elif color == "blue":
        code = "\033[1;34;40m"
    else:
        code = "\033[1;37;40m"

    print(f"{code} {text}")


class Main(webdriver.Edge):
    def __init__(self):
        super(Main, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def lauch_web(self, url):
        printX("yellow", "Step 1/7: Opening Website")
        try:
            self.get(url)
        except:
            printX("!! Failed to open the URL in the browser.", "red")
            self.quit()
        printX("green", ">> Opened Website Successfully")

    def login(self, username, password):
        printX("yellow", "Step 2/7: Trying to Log-In")
        try:
            usernameField = self.find_element(By.NAME, "j_username")
            passwordField = self.find_element(By.NAME, "j_password")
            submitBtn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            usernameField.send_keys(username)
            passwordField.send_keys(password)

            submitBtn.click()
        except:
            printX("red", "!! Could not find the required elements on the web page.")
            self.quit()
        printX("green", ">> Successfully Logged in!")

    def openTestsPage(self):
        printX("yellow", "Step 3/7: Opening Online tests page.")
        try:
            acedemicFnsBtn = self.find_element(By.CSS_SELECTOR, 'a[pid="20009"]')
            acedemicFnsBtn.click()
            onlineAssessmentBtn = self.find_element(
                By.CSS_SELECTOR, 'a[href="stu_studentTest.htm"]'
            )

            wait = WebDriverWait(self, timeout=5)
            wait.until(lambda pause: onlineAssessmentBtn.is_displayed())

            onlineAssessmentBtn.click()
        except:
            printX("red", "!! Failed to Open the Online tests page.")
            self.quit()
        printX("green", ">> Done!")

    def getTests(self):
        printX("yellow", "Step 4/7: Getting all the Tests Info.")
        try:
            container = self.find_element(By.ID, "availableTestDiv")
            self.testsData = container.find_elements(By.TAG_NAME, "tr")
        except:
            printX("red", "!! Failed to gather data of all the tests.")
            self.quit()
        printX("green", ">> Got the Data of all the test.")

    def getSpecificTest(self, testNumber):
        printX("yellow", "Step 5/7: Get the specified test.")
        try:
            self.targetTest = self.testsData[testNumber]
            self.targetTestCols = self.targetTest.find_elements(By.TAG_NAME, "td")
        except:
            printX("red", "!! Could not find the specified test.")
            self.quit()
        printX("green", ">> Got the tests.")
        printX("blue", f">> :: Test Name: {self.targetTestCols[0].text}")
        printX("blue", f">> :: Subject: {self.targetTestCols[1].text}")

    def startTest(self, passwordData=[False]):
        printX("yellow", "Step 6/7: Starting the test.")
        try:
            startBtn = self.targetTestCols[-1].find_element(By.TAG_NAME, "button")
            startBtn.click()

            if passwordData[0]:
                passwordField = self.find_element(By.ID, "txtKeyVerification")
                passwordField.send_keys(passwordData[1])

                verifyBtn = self.find_element(By.ID, "btnSubmitKeyVerification")
                verifyBtn.click()

            time.sleep(1)

            bigStartBtn = self.find_element(By.ID, "idStartTestImg")
            # wait = WebDriverWait(self, timeout=5)
            # wait.until(lambda pause: bigStartBtn.is_displayed())
            bigStartBtn.click()
        except:
            printX("red", "!! Failed to start the test.")
            self.quit()
        printX("green", ">> Started the test.")

    def collectQuestionsAndOptions(self):
        printX("yellow", "Step 7/7: Now collecting all the questions.")
        try:
            quesNumTable = self.find_element(By.ID, "questionImg")
            questionsChips = quesNumTable.find_elements(By.TAG_NAME, "span")
        except:
            printX("red", "!! Could not find the required elements on the web page.")
            self.quit()

        for chip in questionsChips:
            chip.click()

            try:
                parentContainer = self.find_element(By.ID, "questionDiv")
                questionContainer = self.find_element(By.ID, "questionTd")
                questionNumber = questionContainer.find_element(By.TAG_NAME, "span")
                question = questionContainer.find_element(By.TAG_NAME, "b")
                optionBoxes = parentContainer.find_elements(
                    By.CLASS_NAME, "opDivSelectionBox"
                )
            except:
                printX("red", "!! Could not find the required elements on the web page.")
                self.quit()

            try:
                with open("result.txt", "a", encoding="utf-8") as file:
                    file.write(
                        "\n- - - x - - - x - - - x - - - x - - - x - - - x - - -\n\n"
                    )
                    file.write(f"{questionNumber.text}\n")
                    file.write(f"{question.text}\n\n")
                    file.write("Options are:\n\n")
                    for optionBox in optionBoxes:
                        option = optionBox.find_element(By.TAG_NAME, "label")
                        file.write(f"{option.text}\n")
            except:
                printX("red", "!! Unknown exeception occured during writing the file.")
                self.quit()
            # Give some times to chips to be clickable
            time.sleep(1.2)
        
        printX("green", ">> Collected all the questions")
        printX("white", "Script finished!")
        self.quit()
