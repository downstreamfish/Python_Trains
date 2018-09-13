fo = open('test.dat','r')
boy = []
girl = []

for line in fo:
	(role, line_spoken) = line.split('：', 1)
	if role == '男':
		boy.append(line_spoken)
	elif role == '女':
		girl.append(line_spoken)

file_name_boy = 'boy_'+ str(cnt) + '.txt'
file_name_girl = 'girl_' + str(cnt) + '.txt'
boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')
boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
fo.close()
