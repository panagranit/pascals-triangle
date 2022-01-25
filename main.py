''' Try to generate pascals triangle rows '''  
''' brute force avoids Factorials'''
example = [1]
arr =[]
def new_start_row( oldrow):
  new_row = [0]+oldrow + [0]
  return new_row
index = 1



def elementwise_addition(new_row):
  arr = []
  index = 1
  for x in new_row:
    if index != len(new_row):
      #print('x',x,"  ","index",index)
      
      arr.append( x + new_row[index])
      #print ( x + new_row[index])
      index = index + 1
  return arr


''''''''
z = new_start_row(example)
#print(new_start_row(example))

x  = elementwise_addition(z)
#print( x)

''''  add zeros to list then add elements in list to get new list and repeat for k times'''
pp = example
for i in range(100):
  x = new_start_row(pp)
  #print( x)
  pp = elementwise_addition(x)
  
  print (pp)


