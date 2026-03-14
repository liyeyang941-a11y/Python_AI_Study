# 复用之前的商品列表，全程围绕电商场景练习
goods_list = [
    {"id": 1001, "name": "无线鼠标", "price": 99.9},
    {"id": 1002, "name": "机械键盘", "price": 299.0},
    {"id": 1003, "name": "鼠标垫", "price": 19.9}
]
# ----------------------
# 模块1：无参数无返回值的函数
# ----------------------
# 1. 定义函数：def 函数名():  缩进里写函数要做的事
def print_shop_header():
    print("=====================")
    print("  电商商品管理系统  ")
    print("=====================")
    print("ID | 商品名称 | 价格")
    print("---------------------")

# 2. 调用函数：写函数名+()，就会执行函数里的代码
print_shop_header()

# 遍历商品，打印列表
for goods in goods_list:
    print(f"{goods['id']} | {goods['name']} | {goods['price']}元")
    # ----------------------
# 模块2：带位置参数的函数
# ----------------------
# 定义函数：括号里写参数，多个参数用逗号隔开
def calc_discount_price(original_price, discount):
    """
    计算商品折后价
    :param original_price: 商品原价（必填）
    :param discount: 折扣率，比如0.8就是8折（必填）
    """
    # 计算折后价，保留2位小数（符合价格格式）
    final_price = round(original_price * discount, 2)
    print(f"原价{original_price}元，{discount*10}折后：{final_price}元")

# 调用函数，按顺序传入参数
calc_discount_price(99.9, 0.8)  # 无线鼠标8折
calc_discount_price(299.0, 0.75) # 机械键盘75折
calc_discount_price(19.9, 0.5)   # 鼠标垫5折
# ----------------------
# 模块3：带return返回值的函数
# ----------------------
# 1. 定义函数：根据商品ID查找商品，返回找到的商品信息
def find_goods_by_id(goods_id):
    """
    根据商品ID查找商品
    :param goods_id: 要查找的商品ID
    :return: 找到返回商品字典，没找到返回None
    """
    for goods in goods_list:
        if goods["id"] == goods_id:
            return goods  # 找到商品，直接返回商品字典
    return None  # 循环结束没找到，返回None

# 2. 调用函数，用变量接收返回的结果
target_goods = find_goods_by_id(1002)
if target_goods:
    print(f"\n找到商品：{target_goods['name']}，价格{target_goods['price']}元")
else:
    print("\n未找到该商品")

# 3. 进阶：计算订单总价的函数，返回总价
def calc_order_total(goods_id, buy_num):
    """
    计算订单总价
    :param goods_id: 商品ID
    :param buy_num: 购买数量
    :return: 订单总价
    """
    goods = find_goods_by_id(goods_id)
    if not goods:
        return 0
    total = goods["price"] * buy_num
    return round(total, 2)

# 调用：买2个机械键盘，算总价
order_total = calc_order_total(1002, 2)
print(f"订单总价：{order_total}元")
# ----------------------
# 模块4：带默认参数的函数
# ----------------------
# 注意：默认参数必须放在位置参数的后面！
def calc_order_final_price(goods_id, buy_num, discount=0.8, freight=0):
    """
    计算订单最终实付金额
    :param goods_id: 商品ID（必填）
    :param buy_num: 购买数量（必填）
    :param discount: 折扣，默认8折（选填）
    :param freight: 运费，默认0元（选填）
    :return: 最终实付金额
    """
    goods = find_goods_by_id(goods_id)
    if not goods:
        return 0
    # 总价 = 单价*数量*折扣 + 运费
    total = goods["price"] * buy_num * discount + freight
    return round(total, 2)

# 调用1：只传必填参数，用默认折扣和运费
price1 = calc_order_final_price(1001, 1)
print(f"\n默认8折+免运费：{price1}元")

# 调用2：自定义折扣，运费默认0
price2 = calc_order_final_price(1001, 1, discount=0.7)
print(f"自定义7折+免运费：{price2}元")

# 调用3：自定义折扣和运费
price3 = calc_order_final_price(1001, 1, discount=0.9, freight=8)
print(f"9折+8元运费：{price3}元")
# ======================
# 今日练习参考代码
# ======================

# 练习1：新增商品的函数
def add_goods(goods_id, name, price):
    # 先检查ID是否重复
    if find_goods_by_id(goods_id):
        print(f"❌ 商品ID{goods_id}已存在，新增失败")
        return
    # 新增商品
    new_goods = {"id": goods_id, "name": name, "price": price}
    goods_list.append(new_goods)
    print(f"✅ 商品【{name}】新增成功")

# 调用测试
add_goods(1004, "蓝牙耳机", 159.0)
print("新增后的商品列表：", goods_list)

# 练习2：修改商品价格的函数
def update_goods_price(goods_id, new_price):
    goods = find_goods_by_id(goods_id)
    if not goods:
        print(f"❌ 商品ID{goods_id}不存在，修改失败")
        return None
    goods["price"] = new_price
    print(f"✅ 商品【{goods['name']}】价格修改为{new_price}元")
    return goods

# 调用测试
update_goods_price(1004, 139.0)

# 练习3：价格区间筛选函数
def get_goods_by_price_range(min_price, max_price):
    result = []
    for goods in goods_list:
        if min_price <= goods["price"] <= max_price:
            result.append(goods)
    return result

# 调用测试：筛选100-200元的商品
range_goods = get_goods_by_price_range(100, 200)
print("\n100-200元的商品：", range_goods)