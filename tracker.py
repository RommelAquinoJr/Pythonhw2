def func_counter(func):

  def counter():
    counter.count +=1
    
  counter.count = 0
  return func
