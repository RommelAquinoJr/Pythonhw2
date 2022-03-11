def func_counter(func):
  counter.count = 0
  func
  
  def counter():
    counter.count +=1
  return counter
