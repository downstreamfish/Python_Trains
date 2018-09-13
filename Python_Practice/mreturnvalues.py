def profile():
   name = "Danny"
   age = 30
   return (name, age)
def profile2():
   name = "Jackson"
   age = 42
   return name, age

profile_data= profile()
print(profile_data[0])
print(profile_data[1])
print(profile2())
