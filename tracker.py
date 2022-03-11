def func_counter(func):
  func
  
  def counter():
    counter.count +=1
    
  counter.count = 0
  return func_counter()
