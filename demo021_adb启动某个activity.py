import subprocess
import time
from datetime import datetime

# 定义应用包名和目标 Activity 名称
package_name = "com.youxiang.soyoungapp"
activity_name = "com.soyoung.product.ProductDetailV2Activity"
# 定义 Windows 下存储日志的文件路径
log_file_path = f"D:\\360Downloads\\adb_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def clear_logcat():
    """
    清除 logcat 日志
    """
    try:
        subprocess.run("adb logcat -c", shell=True, check=True)
        print("logcat 日志已清除")
    except subprocess.CalledProcessError as e:
        print(f"清除 logcat 日志时出错: {e}")

def get_app_logs():
    """
    获取应用相关的 logcat 日志
    """
    try:
        command = f'adb logcat -d | findstr "{package_name}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8', check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"获取 logcat 日志时出错: {e}")
        return None

def run_adb_activity_start():
    """
    执行 ADB 命令启动指定 Activity
    """
    try:
        command = f"adb shell am start -n {package_name}/{activity_name}"
        subprocess.run(command, shell=True, check=True)
        print(f"已启动 {activity_name}")
    except subprocess.CalledProcessError as e:
        print(f"执行 ADB 命令时出错: {e}")

def log_adb_operations():
    """
    连续 5 次访问指定 Activity 并记录应用日志
    """
    print(f"日志文件路径: {log_file_path}")
    try:
        with open(log_file_path, 'w', encoding='utf-8') as log_file:
            for i in range(5):
                print(f"第 {i + 1} 次尝试访问 {activity_name}")
                # 清除 logcat 日志
                clear_logcat()
                # 启动 Activity
                run_adb_activity_start()
                # 等待一段时间，让应用有足够时间产生日志
                time.sleep(5)
                # 获取应用相关的 logcat 日志
                logs = get_app_logs()
                if logs:
                    log_file.write(f"第 {i + 1} 次访问日志:\n{logs}\n")
                    print(f"第 {i + 1} 次访问日志已写入文件")
    except Exception as e:
        print(f"写入日志文件时出错: {e}")

if __name__ == "__main__":
    log_adb_operations()
