from main import Main
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("ERP_BASE_URL")
username = os.getenv("ERP_USERNAME")
password = os.getenv("ERP_PASSWORD")
testNumber = os.getenv("ERP_TEST_NUMBER")

with Main() as bot:
    bot.lauch_web(base_url)
    bot.login(username, password)
    bot.openTestsPage()
    bot.getTests()
    bot.getSpecificTest(int(testNumber))
    bot.startTest([True, 1234])
    bot.collectQuestionsAndOptions()
    bot.holdBrowser()

# Prompt:
"""
Answer all the question in the order. Strictly tell the answer as the option do not change the language of the option, If the answer does not match any of the options provided, select the most close or probable one. Answer all in one go.
"""
