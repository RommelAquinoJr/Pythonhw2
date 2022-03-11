def func_counter(func):

  def counter():
    counter.count +=1
    func()
  counter.count = 0
  return counter
