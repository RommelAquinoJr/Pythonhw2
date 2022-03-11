def func_counter(func):

  def counter(x):
    counter.count +=1
    return func(x)
  counter.count = 0
  return counter

def function(x):
  return x
