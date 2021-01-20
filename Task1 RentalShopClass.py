#!/usr/bin/env python
# coding: utf-8

# In[4]:


carpool=[{'Cnum':'A1','Ctype':'SUV','Cstate':'in use','Sprice':100,'Lprice':90,'Vprice':80},
         {'Cnum':'A2','Ctype':'SUV','Cstate':'valid','Sprice':100,'Lprice':90,'Vprice':80},
         {'Cnum':'A3','Ctype':'SUV','Cstate':'valid','Sprice':100,'Lprice':90,'Vprice':80},
         {'Cnum':'B4','Ctype':'Sedan','Cstate':'in use','Sprice':50,'Lprice':40,'Vprice':35},
         {'Cnum':'B5','Ctype':'Sedan','Cstate':'valid','Sprice':50,'Lprice':40,'Vprice':35},
         {'Cnum':'B6','Ctype':'Sedan','Cstate':'valid','Sprice':50,'Lprice':40,'Vprice':35},
         {'Cnum':'C7','Ctype':'Hatchback','Cstate':'valid','Sprice':30,'Lprice':25,'Vprice':20},
         {'Cnum':'C8','Ctype':'Hatchback','Cstate':'valid','Sprice':30,'Lprice':25,'Vprice':20},
         {'Cnum':'C9','Ctype':'Hatchback','Cstate':'valid','Sprice':30,'Lprice':25,'Vprice':20},
         {'Cnum':'C10','Ctype':'Hatchback','Cstate':'valid','Sprice':30,'Lprice':25,'Vprice':20}]

#Basic carpool

class RentalShop:   
    def __init__(self,Sname):
        self.Sname=Sname
    
    def RentBill(n):  
        carpool[n].update({'state':'valid'}) # Update the status of the returned car
        print("You return a car successfully")
        
        Rtype=carpool[n]['Ctype']
    
        Rday=int(input('Enter the number of days you have used the car'))
        
        if Rday<0: #Confirm whether the number of days entered by the user is the correct type
            raise TypeError('Please enter the correct number of days')
        
        if Rday > 7: #Determine the number of days entered, and calculate the corresponding fee
            money=carpool[n]['Lprice']*Rday
            return Rtype,Rday,money
        elif Rday <= 7:
            money=carpool[n]['Sprice']*Rday
            
            return [Rtype,Rday,money] #Return result list

    
    def DisStock():
        sum_1=0
        sum_2=0
        sum_3=0
        for i in carpool:           #Find the corresponding type of car whose current status is valid through looping
            if i['Ctype']=='SUV' and i['Cstate']=='valid':
                sum_1+=1
            elif i['Ctype']=='Sedan' and i['Cstate']=='valid':
                sum_2+=1
            elif i['Ctype']=='Hatchback' and i['Cstate']=='valid':
                sum_3+=1
        
        print("Currently available SUV:",sum_1)   #Output current available inventory of various vehicles
        print("Currently available Sendan:",sum_2)
        print("Currently available Hatchback:",sum_3)
        print("****************************************************************************************")
       
        print("Vehicles that can be rented:")  #Output a list of available cars for customers to choose
        for i in carpool:
            if i['Cstate']=='valid':
                print("car number:",i['Cnum'],"   ","car type:",i['Ctype'],"   ","short-term price:",i['Sprice'],"long-term prize:",i['Lprice'])
    
    def CheckRent(n):
        carpool[n].update({'state':'in use'}) #Confirm the rental of the car and change the status to in use
        print("Car is ready")
        
    def VRentBill(n):  
        carpool[n].update({'state':'valid'}) # Update the status of the returned car
        print("You return a car successfully")
        
        Rtype=carpool[n].get('Ctype')#Get the type of returned car
    
        Rday=int(input('Enter the number of days you have used the car'))
        
        if Rday<0: #Confirm whether the number of days entered by the user is the correct type
            raise TypeError('Please enter the correct number of days')
        
        money=carpool[n]['Vprice']*Rday
       
        return [Rtype,Rday,money] #Return result list


# In[ ]:




