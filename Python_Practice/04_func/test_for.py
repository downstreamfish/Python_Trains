students =[
    {'name':'阿土',
     'age':20,
     'gender':True,
     'height':1.7,
     'weight':27.0},
    {'name':'小美',
     'age':19,
     'gender':False,
     'height':1.6,
     'weight':45.0}
    ]

find_name = '小美'

for stu_dict in students:
    print(stu_dict)

    if stu_dict['name'] == find_name:
        print('找到了!')
        break
else:
    print('没找到!')

print('循环结束!')
