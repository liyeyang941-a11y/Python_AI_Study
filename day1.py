# ----------------------
# 1. 定义电商商品变量
# ----------------------
goods_id = 1001          # 商品ID（整数）
goods_name = "无线鼠标"   # 商品名（字符串）
goods_price = 99.9       # 价格（浮点数）
goods_tags = ["办公", "无线", "静音"]  # 标签（列表）

# 商品信息（字典）
goods_info = {
    "id": goods_id,
    "name": goods_name,
    "price": goods_price
}

# ----------------------
# 2. 打印看看
# ----------------------
print("商品信息：", goods_info)

# ----------------------
# 3. 运算：算8折价格
# ----------------------
discount = 0.8
final_price = goods_price * discount
print(f"原价：{goods_price} 元，8折后：{final_price} 元")

# ----------------------
# 4. 判断标签在不在
# ----------------------
print("静音" in goods_tags)
print("游戏" in goods_tags)

# ----------------------
# 5. 输入价格并转数字
# ----------------------
input_str = input("请输入一个商品价格：")
input_price = float(input_str)
print(f"你输入的价格是：{input_price}，类型是：{type(input_price)}")
