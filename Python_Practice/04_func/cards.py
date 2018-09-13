#! /usr/local/bin/python3

import pint_lines as pl
pl.print_line('*', 45)
print("欢迎使用[名片管理系统]V1.0")
print()
print('1. 新建名片')
print('2. 显示全部')
print('3. 查询名片')
print()
print('0. 退出系统')
pl.print_line('*', 45)

cards = []

def create_card():
    global cards
    card = {}
    print("新建名片")
    card['name'] = input("请输入名字: ")
    card['phone'] = input("请输入电话: ")
    card['qq'] = input("请输入QQ: ")
    card['mail'] = input('请输入邮箱: ')
    cards.append(card)

def print_card():
    print("显示名片")
    for card in cards:
        pl.print_line('*', 40)
        print("姓名: ", card['name'])
        print("电话: ", card['phone'])
        print(' Q Q: ', card['qq'])
        print('邮箱: ', card['mail'])
        pl.print_line('*', 40)

def search_card():
    print("查询名片")
    global cards
    find_name = input("输入要查询的姓名")
    for card in cards:
        if find_name == card['name']:
            select = int(input('已找到(要修改:4, 还是删除:5): '))
            if select == 4:
                card['phone'] = input('输入新的电话: ')
                card['qq'] = input("输入新的QQ:")
                card['mail'] = input('输入新的邮箱:')
            elif select == 5:
                cards.remove(card)
            break
    else:
        print("请先添加")

menu = int(input('请输入想要的操作:'))

while menu != 0:
    if menu == 1:
        create_card()
    elif menu == 2:
        print_card()
    elif menu == 3:
        search_card()

    menu = int(input('请输入想要的操作:'))
