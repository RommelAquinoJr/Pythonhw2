import time

def calculate_time(func):
  start = time.time()
  def wrappedFunc():
    func
    end = time.time()
    print(f'Total time {end - start}')
  return wrappedFunc

def foo():
  print("Total time")
  
foo = calculated_time(foo)
