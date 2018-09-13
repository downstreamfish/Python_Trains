from collections import defaultdict
from collections import Counter
colours = (
   ('Yasoob','Yellow'),
   ('Ali','Blue'),
   ('Arham', 'Green'),
   ('Ali', 'Black'),
   ('Yasoob','Red'),
   ('Ahmed', 'Silver')
)

favourite_clours = defaultdict(list)

for name, colour in colours:
   favourite_clours[name].append(colour)

print(favourite_clours)

favs = Counter(name for name, colour in colours)

print(favs)
