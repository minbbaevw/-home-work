name = input ("Введите что-либо: ")
if len (name) < 5:
  print (name.upper())
elif len (name) > 5:
  print (name[::-1])
elif len(name) == 5:
  t = list(name)
  print(t)