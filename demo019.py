import asyncio
import subprocess
import os
import time


async def start_scrcpy_recording(save_path, video_filename="recording.mp4"):
    """使用 scrcpy 录制屏幕，并等待用户手动关闭 scrcpy 窗口后停止录制"""
    # 确保保存路径存在
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 录制命令
    video_save_path_local = os.path.join(save_path, video_filename)

    # 修改为 scrcpy 的完整路径
    scrcpy_path = r"D:\scrcpy-win64-v3.1\scrcpy.exe"  # 根据实际安装路径修改

    # 启动 scrcpy 录制
    command = [
        scrcpy_path,
        "--record", video_save_path_local  # 设置录制文件路径
    ]

    print(f"开始录制视频，保存路径：{video_save_path_local}")

    # 启动 scrcpy 录屏
    process = subprocess.Popen(command)

    # 等待直到 scrcpy 进程结束（即用户手动关闭窗口）
    print("请手动关闭 scrcpy 窗口以停止录制")

    # 轮询检查 scrcpy 进程是否退出
    while True:
        # 如果 scrcpy 进程已退出，退出循环
        if process.poll() is not None:
            print(f"scrcpy 进程已退出，视频录制已停止，文件保存在：{video_save_path_local}")
            break
        await asyncio.sleep(1)  # 每秒钟检查一次

    # 确保子进程完全结束
    process.wait()

    print("程序已结束")


async def main():
    app_package = "com.youxiang.soyoungapp/com.soyoung.module_main.ui.SplashActivity"  # 你的包名和启动 Activity
    save_path = r"D:\2"  # 本地保存录制视频的目录
    video_filename = "recording.mp4"  # 保存的文件名

    # 启动应用
    print(f"启动应用：{app_package}")
    subprocess.run(["adb", "shell", "am", "start", "-n", app_package])

    # 开始录制视频
    await start_scrcpy_recording(save_path, video_filename)


if __name__ == "__main__":
    asyncio.run(main())
