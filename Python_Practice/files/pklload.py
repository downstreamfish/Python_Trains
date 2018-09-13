import pickle
pkl_file = open('data.pkl', 'rb')
data = pickle.load(pkl_file)
print(data)
