import random
import math
#taking inputs
#lowerst value
lower = int(input("Enter the lower number:-"))
#upper value
upper = int(input("Enter the Upper number:-"))
#generating random number between the lower and upper
x=random.randint(lower,upper)
total_chances=math.ceil(math.log(upper-lower+1,2))
print("\n\tyou have only",total_chances,"chances to guss the integer!\n")
#initializing the numberof gusses
count=0
flag=False

#calulate of minumum number of
#gusses depends upon range
while count<total_chances:
    count += 1
    #tacking guessing number as input
    guss=int(input("Guss a numbers:"))
    #testing
    if x==guss:
        print("Congragulation you did it ",count,"try")
        #once gussed loop will break
        flag=True
        break
    elif x>guss:
        print("\t\t!!!!!!!!!!!!!!!!!!!!!!!")
        print("\t\tyou gussed too Small!")
        print("\t\t!!!!!!!!!!!!!!!!!!!!!!!!")
    elif x<guss:
        print("\t\t!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\t\tyou Gussed too High!")
        print("\t\t!!!!!!!!!!!!!!!!!!!!!!!!")
#show the output
if not flag:
    print("\n the number is %d"%x)
    print("\t better luck next Time!..")