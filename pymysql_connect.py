import pymysql

# 数据库连接信息
db_config = {
    "host": "47.93.62.230",
    "port": 3306,
    "user": "lhyd",
    "password": "LHzd@0613",
    "database": "zhealth",  # 数据库名
    "charset": "utf8mb4"
}

try:
    # 建立连接
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # SQL查询
    sql = "SELECT mobile FROM biz_user WHERE name = %s"
    cursor.execute(sql, ('王小可',))

    result = cursor.fetchall()
    if result:
        for row in result:
            print(f"{row[0]}")
    else:
        print("未找到该用户")

except Exception as e:
    print(f"数据库操作失败: {e}")
finally:
    # 关闭连接
    if cursor:
        cursor.close()
    if connection:
        connection.close()