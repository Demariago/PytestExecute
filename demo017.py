import datetime

def calculate_time_difference():
    times = []
    letter = 'A'
    while True:
        time_str = input(f"请输入时间点{letter}（格式为 hh:mm:ss）：")
        try:
            time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
            times.append(time_obj)
        except ValueError:
            print("输入的时间格式不正确，请重新输入。")
            continue
        choice = input("是否继续输入时间值？(Y/N)")
        if choice.upper() == "N":
            break
        letter = chr(ord(letter) + 1)
    if len(times) < 2:
        print("至少需要输入两个时间点。")
        return
    for i in range(1, len(times)):
        time_diff = times[i] - times[i - 1]
        print(f"{chr(65 + i)} - {chr(65 + i - 1)}的时间差值为（其中{chr(65 + i - 1)}={times[i - 1].time()}，"
              f"{chr(65 + i)}={times[i].time()}）："
              f"{time_diff.seconds // 3600:02}:{(time_diff.seconds // 60) % 60:02}:{time_diff.seconds % 60:02}")

if __name__ == "__main__":
    calculate_time_difference()