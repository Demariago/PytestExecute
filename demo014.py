#from datetime import datetime
#now=datetime.today().minute
#print(now)

#import random
#ran=random.randint(7,10)
#if ran==9:
 #   print("完了，是9")
#else:
 #   for a in range(7):
  #    print(ran)



word='bottles'
for beer_num in range(3,0,-1):
    print(beer_num,word,"of beer on the wall")
    print("take one")
    if beer_num==1:
        print("no more beer")
    else:
        new_num=beer_num-1
        if new_num==1:
            word='bottle'
        print(new_num,word,"of beer left")
    print()









