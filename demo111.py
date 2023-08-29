# demaria
# 时间:2023/8/29 18:27
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from ulib.FileUtil import FileUtil
def get_time():
service_chrome_driver = Service(executable_path=f"{FileUtil.get_project_path()}/drivers/chromedriver")
driver = webdriver.Chrome(service=service_chrome_driver)
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")
driver.maximize_window()
sleep(3)
time = driver.execute_script("return performance.timing.loadEventStart-performance.timing.fetchStart")
print(f"页面加载时间： {time}")
driver.quit()
if __name__ == '__main__':
get_time()