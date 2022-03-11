import time

def calculate_time(func):
  start = time.time()
  def wrappedFunc():
    func
    end = time.time()
  return(f'Total time {end - start}')
