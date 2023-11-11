a = int(input("loại xe:"))
b = float(input("số km:"))
c = int(input("thời gian chờ:"))
if c<=5:
    q=0
    print("tiền cờ : miễn phí")
else:
    q=(c-5)*800
    print("tiền chờ:", q,"đồng")
if a==4:
   if b<=0.8:
       s=11000
   if b<=20 and b>=0.8:
       s=12100*b
   if b>=30:
       s=12100*30 + (b-20)*10000
if a==7:
   if b<=0.8:
       s=13000
   if b<=30 and b>=0.8:
       s=14100*b
   if b>=30:
       s=14100*30 + (b-30)*12000
print(" tiền di chuyển",s,"đồng")
r=q+s
print("tiền cước:",r,"đồng")

        