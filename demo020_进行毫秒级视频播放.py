import cv2
import time


def show_video_with_time(video_path, width=640, height=480):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    start_time = time.time()  # 获取播放开始的时间

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 计算当前播放的时间（单位为秒）
        current_time = time.time() - start_time

        # 转换为时分秒毫秒格式
        seconds = int(current_time)
        milliseconds = int((current_time - seconds) * 1000)
        time_display = f"{seconds // 3600:02d}:{(seconds % 3600) // 60:02d}:{seconds % 60:02d}.{milliseconds:03d}"

        # 在视频帧上绘制时间戳
        cv2.putText(frame, time_display, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # 调整视频帧的大小
        frame_resized = cv2.resize(frame, (width, height))  # 调整为你需要的大小

        # 显示帧
        cv2.imshow("Video", frame_resized)

        # 按 `q` 键退出
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# 使用替换后的路径，并调整视频大小
video_path = r"D:\2\recording.mp4"  # 你的录制视频路径
show_video_with_time(video_path, width=720, height=1280)  # 设置为 1280x720

