# ZY-SDPA-Assessment
1. customerclass imports rentalshop calss, main only imports customerclass
2. The basic functions have been implemented, but there is a problem that the information in the carpool list/<bn> 
    cannot be changed through the function. Therefore, when borrowing a car, you can only borrow a vehicle whose 
    current status is available, and returning a car can only return a vehicle whose current status is in use. 
    Attached complete carpool:
    
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
