#demaria001
import datetime

def calculate_time_differences(time_str):
    time_list = time_str.split(',')
    times = [datetime.datetime.strptime(t.strip(), '%H:%M:%S') for t in time_list]
    if len(times) < 2:
        print("至少需要输入两个时间点。")
        return
    for i in range(1, len(times)):
        time_diff = times[i] - times[i - 1]
        print(f"{times[i - 1].time()}和{times[i].time()}之间的时间差为："
              f"{time_diff.seconds // 3600:02}:{(time_diff.seconds // 60) % 60:02}:{time_diff.seconds % 60:02}")

time_input = input("请输入多个时间点，用逗号分隔（格式为 hh:mm:ss）：")
calculate_time_differences(time_input)