a = 5
b = 10

op = '1'

if op == '+':
  res = a + b
elif op == '-':
  res = a - b
elif op == '*':
  res = a * b
elif op == '/':
  res = a / b
else:
  res = ''
  print('Operador Inválido')

print(res)

if a == 5 and b == 10: #and, or
  print('um teste')