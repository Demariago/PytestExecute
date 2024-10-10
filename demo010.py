import os


def add_suffix_to_files(directory, suffix):
    # 获取目录下的所有文件名
    files = os.listdir(directory)

    for file in files:
        # 构造新的文件名
        new_name = file.split('.')[0] + suffix + '.' + file.split('.')[1]

        # 重命名文件
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))


# 指定目录和后缀
directory = r"D:\360MoveData\Users\Demaria\Desktop\归档文件汇总\业务汇总\项目过程资料成果清单--测试组-家庭\《用户操作手册》"

suffix = "操作手册"

# 调用函数
add_suffix_to_files(directory, suffix)
