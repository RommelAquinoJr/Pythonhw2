import time

def calculate_time():
  start = time.time()
  main()
  end = time.time()
  print(f'Total time {end - start}')
