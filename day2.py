goods_list = [
    {"id": 1001,'name':'无线鼠标','price':99.9 },
    {'id': 1002,'name':'机械键盘','price':299.0},
    {"id": 1003, "name": "鼠标垫", "price": 19.9}
]
# 先打印一下，确认数据没问题
print("商品列表：", goods_list)
# ----------------------
# 模块2：if 判断商品档次
# ----------------------
print("\n===== 1. 商品档次判断 =====")
# 取第2个商品（索引是1）：机械键盘
target_goods = goods_list[1]

if target_goods["price"] > 200:
    print(f"{target_goods['name']} → 高端商品")
elif target_goods["price"] > 50:
    print(f"{target_goods['name']} → 中端商品")
else:
    print(f"{target_goods['name']} → 平价商品")
    # ----------------------
# 模块3：for 循环筛选平价商品
# ----------------------
print("\n===== 2. 平价商品列表（<100元） =====")
# 遍历每一个商品
for goods in goods_list:
    # 判断价格是否小于100
    if goods["price"] < 100:
        print(f"- {goods['name']}：{goods['price']} 元")
        # ----------------------
# 模块4：while 循环持续查询
# ----------------------
print("\n===== 3. 价格查询工具（输入q退出） =====")
while True:
    # 1. 让用户输入
    user_input = input("请输入价格上限（输入q退出）：")
    
    # 2. 判断是否退出
    if user_input == "q":
        print("👋 退出查询")
        break  # 跳出循环
    
    # 3. 把输入的字符串转成数字
    max_price = float(user_input)
    
    # 4. 筛选并打印
    print(f"\n价格 ≤ {max_price} 元的商品：")
    for goods in goods_list:
        if goods["price"] <= max_price:
            print(f"- {goods['name']}")