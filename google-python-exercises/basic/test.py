def donuts(count):
 
 if count > 10:
     s= ("Number of donuts: many")
 else:
     s=("number of donuts", count)
 
 return str(s)
test =  donuts(5)
print(test)