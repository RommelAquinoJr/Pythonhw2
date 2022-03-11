def func_counter(func):
  print("potato")
  counter.count = 0
  def counter():
    counter.count +=1
  
  return counter
