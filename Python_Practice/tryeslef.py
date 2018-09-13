try:
   print("I am sure no exception is going to occur")

except Exception:
   print('excetion')
else:
   print("This would only run if no exception occurs, And an error here "
         "would  NOT be caught")
finally:
   print("This would be printed in every case")
