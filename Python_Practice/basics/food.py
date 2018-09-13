edibles = ['ham', 'spam', 'eggs', 'nuts']
for food in edibles:
    if food == 'spam':
        print('No more spam please!')
        break
    print("Great, delicious " + food)
else:
    print('I am so glad: No spam!')

print("finally, I finished stuffing myself")
