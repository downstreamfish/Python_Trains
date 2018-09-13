# 含有所有名片的功能函数
# 将对名片的新增/查询/修改/删除等操作封装在不同的函数中
# 所有名片记录的列表
cards_list = []


def show_menu():
    """显示菜单
    """
    print('*' * 50)
    print("欢迎使用[名片管理系统]V1.0")
    print('')
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print('')
    print("0. 退出系统")
    print('*' * 50)


def new_card():
    """新建名片
    """
    print('-' * 50)
    print("功能: 新建名片")

    # 1. 提示用户输入名片信息
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    qq = input("请输入 QQ 号码: ")
    email = input("请输入邮箱: ")

    # 2. 将用户信息保存到一个字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    # 3. 将用户字典添加到名片列表
    cards_list.append(card_dict)
    print(cards_list)

    # 4. 提示添加成功
    print("成功添加{0}的名片".format(card_dict['name']))


def show_all():
    """显示全部
    """
    print('-' * 50)
    print("功能: 显示全部")

    # 1. 判断是否有名片记录
    if len(cards_list) == 0:
        print('提示:没有任何名片记录')
        return

    # 打印表头
    for name in ['姓名', '电话', 'QQ', '邮箱']:
        print(name, end="\t\t")

    print('')

    # 打印分割线
    print('=' * 50)

    for card_dict in cards_list:
        print("{0}\t\t{1}\t\t{2}\t\t{3}".format(card_dict['name'],
                                                card_dict['phone'],
                                                card_dict['qq'],
                                                card_dict['email']))


def search_card():
    """搜索名片
    """
    print('-' * 50)
    print("功能: 搜索名片")
    # 1.提示要搜索的姓名
    find_name = input("请输入要搜索的姓名: ")

    # 2. 遍历字典
    for card_dict in cards_list:
        if card_dict['name'] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print('-' * 50)

            print("{0}\t\t{1}\t\t{2}\t\t{3}".format(card_dict['name'],
                                                    card_dict['phone'],
                                                    card_dict['qq'],
                                                    card_dict['email']))
            print('-' * 50)

            # TODO(小美)针对找到的字典进行后续操作: 修改/删除
            deal_find(card_dict)
            break
    else:
        print("没有找到:", find_name)


def deal_find(find_dict):
    """操作搜索到的名片字典
    :param find_dict: 找到的名片字典
    """
    print(find_dict)
    action_str = input("选择要执行的操作"
                       "[1] 修改 [2] 删除 [0] 返回上级菜单: ")

    if action_str == '1':
        find_dict['phone'] = input_card_info(find_dict['phone'], "请输入新的电话:")
        find_dict['qq'] = input_card_info(find_dict['qq'], "请输入新的QQ号码:")
        find_dict['email'] = input_card_info(find_dict['email'], "请输人新的邮箱:")
    elif action_str == '2':
        cards_list.remove(find_dict)


def input_card_info(dict_value, tip_message):
    """输入名片信息
    :param dict_value:字典原有值
    :param tip_message:输入提示信息
    :return: 如果输入,返回输入内容, 否则返回字典原有值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断,如果用户输入了内容,直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3. 如果用户没有输入内容,返回字典原有的值
    else:
        return dict_value
