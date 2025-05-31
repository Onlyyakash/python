def func1():
  try:
      l = [1, 5, 6, 7]
      i = int(input("enter a number: "))
      print(l[i])
      return 1
  except :
      print("Index out of range")
      return 0
  finally:
      print("I am always executed")
x = func1()
print(x)