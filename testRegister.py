import pymysql

def register(flag):
    # 使用with语句确保数据库连接在使用完毕后自动关闭
    with pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='game_system') as db:
        cursor = db.cursor()

        # 查询所有制造商
        cursor.execute("SELECT id, introduction FROM manufacturer")

        # 获取所有制造商的id和简介
        all_manufacturers = cursor.fetchall()

        # 检查输入的flag是否有效
        if 0 <= flag - 1 < len(all_manufacturers):
            # 获取第flag个厂商的简介
            manufacturer_id = all_manufacturers[flag - 1][0]
            manufacturer_introduction = all_manufacturers[flag - 1][1]
            print(f"第{flag}个厂商的ID为{manufacturer_id}")
            print(f"第{flag}个厂商的简介为{manufacturer_introduction}")
        else:
            print("输入的编号无效，请输入一个有效的厂商编号。")

if __name__ == '__main__':
    i = int(input("请输入查询的厂商编号："))
    try:
        register(i)
    except pymysql.err.DataError:
        print("输入的编号格式不正确，请输入一个整数。")