import pandas  as pd
# 加载Excel文件
excel_file = r'D:\360MoveData\Users\Demaria\Desktop\11.xlsx'
df1 = pd.read_excel(excel_file, sheet_name='Sheet1')
df2 = pd.read_excel(excel_file, sheet_name='Sheet2')

# 取第一列并去重
unique_df1 = df1[df1.columns[0]].drop_duplicates()
unique_df2 = df2[df2.columns[0]].drop_duplicates()

# 找出Sheet1中比Sheet2多出的数据
extra_in_df1 = unique_df1.difference(unique_df2)

print("Sheet1中比Sheet2多出的数据如下：")
print(extra_in_df1)