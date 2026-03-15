# day04.py

# 复用商品列表
goods_list = [
    {"id": 1001, "name": "无线鼠标", "price": 99.9},
    {"id": 1002, "name": "机械键盘", "price": 299.0},
    {"id": 1003, "name": "鼠标垫", "price": 19.9}
]

# 复用昨天的查找函数
def find_goods_by_id(goods_id):
    for goods in goods_list:
        if goods["id"] == goods_id:
            return goods
    return None
# ----------------------
# 模块1：列表/字典进阶操作
# ----------------------
print("===== 1. 列表/字典进阶操作 =====")

# 1.1 列表进阶方法
# 新增商品：append() - 在列表末尾添加
new_goods={'id':1004,'name':'蓝牙耳机','price':159.0}
goods_list.append(new_goods)
print('新增后商品列表:',goods_list)
# 删除商品：remove() - 根据元素值删除
# 先找到要删除的商品，再remove
target=find_goods_by_id(1003)
if target:
    goods_list.remove(target)
    print('删除鼠标垫后:',goods_list)

# 1.2 字典进阶方法
# 遍历字典的3种方式
print('\n遍历所有商品:')
for goods in goods_list:
 # 方式1：直接遍历字典，取key
 print('商品ID:',goods['id'])
 # 方式2：items() - 同时取key和value（最常用）
 for key,value in goods.items():
    print(f'{key}:{value}')
# 方式3：keys()/values() - 单独取key或value
print('商品名称:',goods['name'])

# 1.3 列表切片：取部分商品
print("\n前2个商品:",goods_list[:2])
print('后2个商品:',goods_list[-2:])
# ----------------------
# 模块2：异常处理
# ----------------------
print("\n===== 2. 异常处理 =====")

# 2.1 捕获ValueError：用户输入非数字
try:
    user_input = input("请输入商品ID（数字）：")
    goods_id = int(user_input)  # 可能报错：输入的是文字
    print(f"你输入的ID是：{goods_id}")
except ValueError:
    print("❌ 错误：请输入数字格式的ID！")
# 2.2 捕获KeyError：字典key不存在
try:
    goods=goods_list[0]  # 取第一个商品
    print(goods['stock'])  # 可能报错：字典里没有stock这个key
except KeyError:
    print("❌ 错误：请输入数字格式的ID！")\
# 2.3 捕获IndexError：列表索引越界
try:    print(goods_list[10])  # 可能报错：列表里没有第11个元素
except IndexError:
    print("❌ 错误：列表索引越界！")
# 2.4 完整的异常处理：结合商品查找
try:
    user_input=input("\n请输入要查找的商品ID：")
    goods_id=int(user_input)  # 转数字，可能报错
    goods=find_goods_by_id(goods_id)  # 查找商品
    if goods:
        print("✅ 找到商品：",goods)
    else:
        print("❌ 没有找到该ID的商品！")
except ValueError:
    print("❌ 错误：请输入数字格式的ID！")
except Exception as e:  # 捕获其他未知错误
    print("❌ 发生未知错误：",e)
# ----------------------
# 模块3：整合优化商品管理
# ----------------------
print("\n===== 3. 整合优化商品管理 =====")

# 优化后的新增商品函数（加异常处理）
def add_goods_safe():
    try:
        user_input=input("请输入新商品信息（格式：ID,名称,价格）：")
        id_str,name_str,price_str=user_input.split(',')  # 分割输入
        new_goods={
            'id':int(id_str),  # 转数字，可能报错
            'name':name_str,
            'price':float(price_str)  # 转数字，可能报错
        }
        goods_list.append(new_goods)
        print("✅ 新增商品成功！当前商品列表：",goods_list)
    except ValueError:
        print("❌ 错误：请输入正确格式的商品信息！")
    except Exception as e:
        print("❌ 发生未知错误：",e)
# 优化后的删除商品函数（加异常处理）
def delete_goods_safe():
    try:
        user_input=input("请输入要删除的商品ID：")
        goods_id=int(user_input)  # 转数字，可能报错
        target=find_goods_by_id(goods_id)
        if target:
            goods_list.remove(target)
            print("✅ 删除商品成功！当前商品列表：",goods_list)
        else:
            print("❌ 没有找到该ID的商品！")
    except ValueError:
        print("❌ 错误：请输入数字格式的ID！")
    except Exception as e:
        print("❌ 发生未知错误：",e)
# 测试调用
add_goods_safe()
delete_goods_safe()
print("\n最终商品列表：",goods_list)
print("\n最终商品列表：",goods_list)

# 新增：修改商品名称函数
def update_goods_name():
    try:
        user_input = input("请输入要修改名称的商品ID和新名称（格式：ID,新名称）：")
        id_str, new_name = user_input.split(',')
        goods_id = int(id_str)
        goods = find_goods_by_id(goods_id)
        if goods:
            goods['name'] = new_name
            print("✅ 商品名称修改成功！修改后商品：", goods)
            return goods
        else:
            print("❌ 没有找到该ID的商品！")
            return None
    except ValueError:
        print("❌ 错误：请输入正确格式的商品信息！")
        return None
    except Exception as e:
        print("❌ 发生未知错误：", e)
        return None

update_goods_name()

# 新增：计算所有商品总价值
def calc_total_value():
    total = 0
    for goods in goods_list:
        total += goods['price']
    return total

# 测试调用
print("所有商品总价值：", calc_total_value())


# 新增：根据价格区间查找商品
def find_goods_by_price_range():
    try:
        user_input = input("请输入价格区间（格式：min_price,max_price）：")
        min_str, max_str = user_input.split(',')
        min_price = float(min_str)
        max_price = float(max_str)
        result = []
        for goods in goods_list:
            if min_price <= goods['price'] <= max_price:
                result.append(goods)
        print(f"价格在{min_price}~{max_price}区间的商品：", result)
        return result
    except ValueError:
        print("❌ 错误：请输入数字格式的价格区间！")
        return []
    except Exception as e:
        print("❌ 发生未知错误：", e)
        return []

# 测试调用
find_goods_by_price_range()
 # day04.py