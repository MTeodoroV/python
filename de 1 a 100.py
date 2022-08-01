import time
print("De 1 a 100 com while:") 
i=1
vect =[]
while(i <=100):
    print(i)
    i += 1
    time.sleep(0.20)

print("De 100 a 1 com for:")
for j in range(100,0,-1):
    vect.append(j)
print(vect)