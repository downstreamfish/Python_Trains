import pickle
data = [1, 3 ,5,'张飞',['赵云']]
pickle_file = open('data.pkl','wb')
pickle.dump(data, pickle_file)

pickle_file.close()
