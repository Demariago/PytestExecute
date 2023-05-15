# demaria
# 时间:2023/4/21 10:24
"""
8个位置bit为一个字节byte，即8bit=1byte，同时1024byte=1kb，1024kb=1M
#一个位置2个状态，8个位置为256个状态，一个bit标识256个状态
#ASCII表将128个状态标记
#二进制--ASCII表--GB2312--GBK--GB18030--unicode--utf8 演变的格式变化
"""
#举例
print(chr(0b100111001011000))#该二进制为unicode的乘的二进制展示，注意0b
print(chr(20056))
print(ord('乘'))
#chr和ord刚好是对应的 字符串和原始值
#计算机只识别二进制
