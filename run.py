from main import Main
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("ERP_BASE_URL")
username = os.getenv("ERP_USERNAME")
password = os.getenv("ERP_PASSWORD")

with Main() as bot:
    bot.lauch_web(base_url)
    bot.erpLogin(username, password)
    bot.openTestsPage()
    bot.getTests()
    bot.getSpecificTest(5)
    bot.startTest()
    bot.collectQuestionsAndOptions()