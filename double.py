def doubler(func):
   def wrapper_double():
      func()
      func()
   return wrapper_double
