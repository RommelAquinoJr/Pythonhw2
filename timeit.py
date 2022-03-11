import time

def calculate_time(func):
  start = time.time()
  func.main()
  end = time.time()
  print(f'Total time {end - start}')
