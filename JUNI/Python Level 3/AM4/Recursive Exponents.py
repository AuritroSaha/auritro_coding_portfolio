# main.py

def exponent(x,y):
  if y == 0:
    return 1
  return exponent(x,y-1)*x

print(exponent(3,3))