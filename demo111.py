# demaria
# 时间:2023/8/29 18:27
from time import perf_counter
from selenium import webdriver


def get_page_load_time(url):
    # 创建 Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 设置无界面模式
    driver = webdriver.Chrome(options=options)

    try:
        # 记录开始加载时间
        start_time = perf_counter()

        # 打开页面
        driver.get(url)

        # 等待页面加载完成
        driver.implicitly_wait(10)  # 设置隐式等待时间，单位为秒

        # 计算页面加载时间
        end_time = perf_counter()
        load_time = end_time - start_time

        return load_time

    finally:
        # 关闭 WebDriver
        driver.quit()


# 测试页面的 URL
url = "https://www.baidu.com"  # 替换为您要测试的页面 URL
load_time = get_page_load_time(url)

print(f"页面加载时间：{load_time} 秒")
