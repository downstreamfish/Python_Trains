#! /usr/bin/python3


class HouseItem:
    ''' 家具类

    : param name：家具名称
    : param area: 占地面积
    '''

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具%s, 占地 %.2f 平米" % (self.name, self.area)


class House:
    ''' 房子类
    '''

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("房子户型%s, 总面积%.2f, 剩余面积%.2f, 家具有：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        self.item_list.append(item.name)
        self.free_area = self.free_area - item.area


a_bed = HouseItem('席梦思', 4)
a_chest = HouseItem('衣柜', 2)
a_table = HouseItem('餐桌', 1.5)
a_house = House("四室一厅", 100)
a_house.add_item(a_bed)
a_house.add_item(a_chest)
a_house.add_item(a_table)

print(a_house)
