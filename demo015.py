from datetime import datetime, time

def input_time():
    while True:
        user_input = input("请输入时间 (HH:MM:SS 格式): ")
        try:
            # 尝试解析用户输入的时间
            return datetime.strptime(user_input, "%H:%M:%S").time()
        except ValueError:
            print("无效的时间格式，请重新输入！")

def time_difference(time_a, time_b):
    # 将时间转换为datetime对象，以便可以进行减法运算
    date_today = datetime.today().date()
    dt_a = datetime.combine(date_today, time_a)
    dt_b = datetime.combine(date_today, time_b)

    # 计算时间差
    delta = dt_a - dt_b
    return delta

# 输入第一个时间点
print("请输入第一个时间 A:")
time_a = input_time()

# 输入第二个时间点
print("请输入第二个时间 B:")
time_b = input_time()

# 计算时间差
delta = time_difference(time_a, time_b)

# 输出结果
print(f"时间差为: {delta}")

