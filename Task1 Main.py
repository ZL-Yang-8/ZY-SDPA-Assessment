#!/usr/bin/env python
# coding: utf-8

# In[1]:


from CustomerClass import *

start=int(input('please input your choice 1.Inquire 2.rent a car 3.returen a car 4.VIP return a car')) 

a=Customer(1,"a")#Instantiate object
b=VCustomer(CusNum=2,CusName="b")
c=RentalShop("RS")

if start==1:
    a.Inquire()
elif start==2:
    a.RentCar()
elif start==3:
    a.ReturnCar()
elif start==4:
    b.VReturnCar()
else:
    print("input a correct number")


# In[ ]:




