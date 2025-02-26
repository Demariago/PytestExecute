from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "deviceName": "D3H7N17C06002576",
    "appPackage": "com.youxiang.soyoungapp",
    "appActivity": "com.soyoung.module_main.ui.MainActivityV2",
    "language": "en",
    "locale": "US",
    "noReset": True
}

print("Desired caps:", desired_caps)

# 再次确认 desired_caps 不为 None
if desired_caps is not None:
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("App 已成功启动")
        time.sleep(10)
    except Exception as e:
        print(f"启动 App 时出现错误: {e}")
    finally:
        if 'driver' in locals() and driver:
            driver.quit()
else:
    print("desired_caps 为 None，无法启动 App。")