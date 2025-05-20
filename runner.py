import subprocess
import os

allure_results_dir = "reports/allure-results"

command_pytest = [
    "pytest",
    "test/smoke/КАКОЕ ТО НАЗВАНИЕ В БУДУЩЕМ", # ДОБАВИТЬ НАЗВАНИЕ АКТИВИРУЕМОГО .py
    "--browser=firefox",
    "--headless",
    "--alluredir=" + allure_results_dir,
]

command_allure = [
    "allure",
    "serve",
    allure_results_dir,
]

result = subprocess.run(command_pytest)
report = subprocess.run(command_allure)

exit(result.returncode)