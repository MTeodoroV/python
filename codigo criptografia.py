msg = input("Digite uma mensagem:")
msg2 = ""
for x in msg:
  y = ord(x)+1
  msg2=msg2+chr(y)
print(msg2)
msg=""
for x in msg2:
  y = ord(x)-1
  msg=msg+chr(y)
print(msg)