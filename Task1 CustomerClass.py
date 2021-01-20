#!/usr/bin/env python
# coding: utf-8

# In[1]:


from RentalShopClass import * #Need to call the method in the RentalShop class
class Customer:
    
    def __init__(self,CusNum,CusName):
        self.CusNum=CusNum  
        self.CusName=CusName

    def Inquire(self):
        return RentalShop.DisStock() #Provide an interface to return query results

    def RentCar(self):  
        Rcar = input('Enter the number of the car you want to rent ')
        
        cl=['A1','A2','A3','B4','B5','B6','C7','C8','C9','C10'] #Raise exception to ensure that the input type is correct
        if Rcar not in cl:
            raise TypeError('Please enter the correct car number')
            
        n=0 # Mark the current traverse position
        for i in carpool: #Find available car according to the car number
            n+=1
            if i['Cnum'] == Rcar :
                if i['Cstate']=='valid':
                    print('You can rent this car')
                    RentalShop.CheckRent(n-1) #Arouse the functions in the rental shop class to change the rented car status
                else:
                    print('Vehicle unavailable')
                    

    def ReturnCar(self):
        Rcar = input('Enter the number of the car you want to return ')
        
        cl=['A1','A2','A3','B4','B5','B6','C7','C8','C9','C10'] #Raise exception to ensure that the input type is correct
        if Rcar not in cl:
            raise TypeError('Please enter the correct car number')
            
        n=0
        for i in carpool:
            n+=1
            if i['Cnum'] == Rcar :
                if i['Cstate']=='in use':
                    Tbill=RentalShop.RentBill(n-1)  #Arouse the functions in the rental shop class to get bill information
                    print("You have rented a",Tbill[0],"for",Tbill[1],"days." " You will be charged GBP",Tbill[2],",We hope that you enjoy our service.")
                else :
                    print("This car is not in use")


# In[2]:


class VCustomer(Customer):
    def __init__(self,CusNum,CusName):
        super().__init__(CusNum,CusName) # Inherit the customer number in the parent class
        self.CusNum=CusNum
        self.CusName=CusName
    
    def VReturnCar(self):
        Rcar = input('Enter the number of the car you want to return ')
        
        cl=['A1','A2','A3','B4','B5','B6','C7','C8','C9','C10'] #Raise exception to ensure that the input type is correct
        if Rcar not in cl:
            raise TypeError('Please enter the correct car number')
            
        n=0
        for i in carpool:
            n+=1
            if i['Cnum'] == Rcar :
                if i['Cstate']=='in use':
                    Tbill=RentalShop.VRentBill(n-1)  #Arouse the functions in the rental shop class to get bill information
                    print("Dear VIP,you have rented a",Tbill[0],"for",Tbill[1],"days." " You will be charged GBP",Tbill[2],",We hope that you enjoy our service.")
                else :
                    print("This car is not in use")

