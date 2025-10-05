import subprocess
import os
import sys
import shutil

def run_tests():
    # Очистка старых результатов
    allure_results = "allure-results"
    if os.path.exists(allure_results):
        shutil.rmtree(allure_results)
    
    # Запуск pytest
    cmd = [
        sys.executable, "-m", "pytest",
        "test/smoke/test_test.py",
        "-v",
        "--browser=chrome",
        f"--alluredir={allure_results}"
    ]
    
    print("Запуск:", " ".join(cmd))
    result = subprocess.run(cmd)
    
    # Генерация отчёта только если тесты прошли
    if result.returncode in [0, 1, 2, 5]:  # Коды успеха pytest
        if os.path.exists(allure_results) and os.listdir(allure_results):
            print("Генерация Allure отчёта...")
            subprocess.run([sys.executable, "-m", "allure", "serve", allure_results])
        else:
            print("Нет результатов для отчёта")
    
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)