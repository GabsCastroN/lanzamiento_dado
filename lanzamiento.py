import random 

print("---------------------------------")
print("-------------Dado----------------")
print("---------------------------------")

a = random.randint(0,6)

if (a==1):
    rta = "uno"
elif (a==2):
    rta = "dos"
elif (a==3):
    rta = "tres"
elif (a==4):
    rta = "cuatro"
elif (a==5):
    rta = "cinco"
elif (a==6):
    rta = "seis"
else:
    rta="no es un dado"


print("dado 1: " + str(rta))