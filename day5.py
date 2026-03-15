# day05.py

# 先导入csv模块（Python自带，不用安装）
import csv

# 复用商品列表
goods_list = [
    {"id": 1001, "name": "无线鼠标", "price": 99.9},
    {"id": 1002, "name": "机械键盘", "price": 299.0},
    {"id": 1003, "name": "鼠标垫", "price": 19.9}
]

# 复用查找函数
def find_goods_by_id(goods_id):
    for goods in goods_list:
        if goods["id"] == goods_id:
            return goods
    return None
# ----------------------
# 模块1：文本文件读写
# ----------------------
print("===== 1. 文本文件读写 =====")

# 1.1 写入文本文件（w模式：覆盖写入）
# with open会自动关闭文件，不用手动close
with open("goods.txt", "w", encoding="utf-8") as f:
    for goods in goods_list:
        line = f"{goods['id']},{goods['name']},{goods['price']}\n"
        f.write(line)
print("已写入 goods.txt 文件")

# 1.2 读取文本文件（r模式：只读）
with open("goods.txt", "r", encoding="utf-8") as f:
 # 方式1：read() 读取全部
    content = f.read()
    print("文件内容（read）：")
    print(content)
# 方式2：readlines() 读取为行列表
    f.seek(0)  # 回到文件开头
    lines = f.readlines()
    print("文件内容（readlines）：")
    print(lines)

# 1.3 追加写入（a模式：在文件末尾添加）
with open("goods_names.txt", "a", encoding="utf-8") as f:
    f.write("蓝牙耳机\n")
print("\n✅ 已追加蓝牙耳机到文件")
# ----------------------
# 模块2：CSV文件读写
# ----------------------
print("\n===== 2. CSV文件读写 =====")
# 定义CSV文件路径
csv_file = "goods.csv"
# 定义表头
header = ["id", "name", "price"]
# 2.1 写入CSV文件
def save_goods_to_csv():
    """把商品列表保存到CSV文件"""
with open(csv_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()  # 写入表头
    writer.writerows(goods_list)  # 写入多行数据
print("已写入 goods.csv 文件")
# 调用保存函数
save_goods_to_csv()
# 2.2 读取CSV文件
def load_goods_from_csv(file_path):
    """从CSV文件读取商品数据到goods_list"""
    global goods_list
    goods_list = []  # 清空原有列表
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV读出来的都是字符串，需要转换数据类型
                goods = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "price": float(row["price"])
                }
                goods_list.append(goods)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

# 调用读取函数
load_goods_from_csv(csv_file)
print("从CSV文件加载的商品列表：", goods_list)

# ----------------------
# 模块3：整合优化商品管理
# ----------------------
print("\n===== 3. 整合优化商品管理 =====")

# 优化后的新增商品函数（自动保存）
def add_goods_and_save():
    try:
        goods_id = int(input("请输入商品ID："))
        if find_goods_by_id(goods_id):
            print("❌ 该ID已存在！")
            return
        name = input("请输入商品名称：")
        price = float(input("请输入商品价格："))
        goods_list.append({"id": goods_id, "name": name, "price": price})
        save_goods_to_csv()  # 新增后自动保存
        print(f"✅ 商品【{name}】新增并保存成功！")
    except ValueError:
        print("❌ 错误：ID和价格必须是数字！")

# 优化后的删除商品函数（自动保存）
def delete_goods_and_save():
    try:
        goods_id = int(input("请输入要删除的商品ID："))
        goods = find_goods_by_id(goods_id)
        if goods:
            goods_list.remove(goods)
            save_goods_to_csv()  # 删除后自动保存
            print(f"✅ 商品【{goods['name']}】删除并保存成功！")
        else:
            print("❌ 未找到该商品！")
    except ValueError:
        print("❌ 错误：ID必须是数字！")

# 修改商品价格函数（自动保存）
def update_goods_price(goods_id, new_price):
    try:
        goods = find_goods_by_id(goods_id)
        if goods:
            goods['price'] = float(new_price)
            save_goods_to_csv()  # 修改后自动保存
            print(f"✅ 商品【{goods['name']}】价格更新并保存成功！")
        else:
            print("❌ 未找到该商品！")
    except ValueError:
        print("❌ 错误：价格必须是数字！")

# 查询商品函数
def query_goods():
    try:
        goods_id = int(input("请输入要查询的商品ID："))
        goods = find_goods_by_id(goods_id)
        if goods:
            print(f"商品ID：{goods['id']}")
            print(f"商品名称：{goods['name']}")
            print(f"商品价格：{goods['price']}")
        else:
            print("❌ 未找到该商品！")
    except ValueError:
        print("❌ 错误：ID必须是数字！")

# 测试调用
# load_goods_from_csv()  # 先读取已有数据
# add_goods_and_save()
# delete_goods_and_save()
# print("最终商品列表：", goods_list)
# update_goods_price(1001, 109.9)

# 从 CSV 读取数据后统计商品数量和总价值
load_goods_from_csv(csv_file)
print(f"商品数量：{len(goods_list)}")
total_value = sum(goods['price'] for goods in goods_list)
print(f"总价值：{total_value}")

# 菜单循环
while True:
    print("\n菜单：")
    print("1. 新增商品")
    print("2. 删除商品")
    print("3. 查询商品")
    print("4. 退出")
    choice = input("请选择（1-4）：")
    if choice == '1':
        add_goods_and_save()
    elif choice == '2':
        delete_goods_and_save()
    elif choice == '3':
        query_goods()
    elif choice == '4':
        print("退出程序")
        break
    else:
        print("❌ 无效选择，请重新输入")

