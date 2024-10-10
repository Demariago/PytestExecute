import json
import os

def adjust_times(data, unified_start_time_ms, first_submit_time_ms):
    """遍历并调整时间字段，确保submitTime递增10秒"""
    submit_time_offset = first_submit_time_ms - unified_start_time_ms
    submit_time_ms = first_submit_time_ms
    def process_item(obj):
        nonlocal submit_time_ms
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'startTime':
                    obj[key] = unified_start_time_ms
                elif key == 'submitTime':
                    obj[key] = submit_time_ms
                    submit_time_ms += 300000  # 增加10秒，转换为毫秒
                elif isinstance(value, (dict, list)):
                    process_item(value)
        elif isinstance(obj, list):
            for item in obj:
                process_item(item)

    process_item(data)

# 用户输入
unified_start_time_input = input("请输入所有startTime的统一毫秒值: ")
try:
    unified_start_time_ms = int(unified_start_time_input)
except ValueError:
    print("输入无效，请输入一个整数。")
    exit()

first_submit_time_input = input("请输入第一个submitTime的毫秒值: ")
try:
    first_submit_time_ms = int(first_submit_time_input)
except ValueError:
    print("输入无效，请输入一个整数。")
    exit()

json_file_path = input("请输入JSON文件的完整路径: ")

if not os.path.exists(json_file_path):
    print("文件路径不存在，请检查后重新输入。")
    exit()

# 读取并处理JSON数据
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

adjust_times(data, unified_start_time_ms, first_submit_time_ms)

# 输出或保存修改后的JSON数据
print(json.dumps(data, indent=2))

# 可以将修改后的内容写回到文件中
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)