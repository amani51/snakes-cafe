'''
This is a Snakes Cafe project
users should order from our menu or they will get a message to correct their order
user can make orders multiple times 
each time users order, their order will appear 
once they write quit the order will complete, and a summary of the complete order will print out 
'''
a= '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
'''

menu=[{
    "name":"Appetizers",
    "options":["Wings", "Cookies Spring", "Rolls"],
    "numbers_of_order":[0,0,0]
},{
    "name":"Entrees",
    "options":["Salmon", "Steak", "Meat Tornado","A Literal Garden"],
    "numbers_of_order":[0,0,0,0]
},{
    "name":"Desserts",
    "options":["Ice Cream", "Cake", "Pie"],
    "numbers_of_order":[0,0,0]
},{
    "name":"Drinks",
    "options":["Coffee", "Tea", "Unicorn Tears"],
    "numbers_of_order":[0,0,0]
},
]

def order_fun(x):
    test=[]
    for i in range(len(menu)):
            for j in range(len(menu[i]["options"])):
                if order==menu[i]["options"][j]:
                    test.append((order))
                    menu[i]["numbers_of_order"][j]+=1
                    if menu[i]["numbers_of_order"][j]==1:
                        print(f'** {menu[i]["numbers_of_order"][j]} order of {order} have been added to your meal **')
                        print("so your order will be: ")
                        print(f'***********************************') 
                        print(total(x,order))
                        print(" anything else , or 'quit' for finish ")
                    else:
                        print(f'** {menu[i]["numbers_of_order"][j]} orders of {order} have been added to your meal **')
                        
                        print("so your order will be: ")
                        print(f'***********************************') 
                        print(total(x,order))
                        print(" add anything else , or 'quit' for finish ")
    if test==[]:
        print('Please choose your order from the menu with the correct words!!') 
    return x

def total(x,order): 
             
    for i in range(len(menu)):
            for j in range(len(menu[i]["options"])):
                if menu[i]["numbers_of_order"][j]!=0:
                    x+=f'{menu[i]["numbers_of_order"][j]} of {menu[i]["options"][j]}, ' 
                
    if x!="" and order!="quit":
        return (f'=> {x}')
    elif x!="" and order=="quit":
        print("** Thank you for visiting our restaurant **" )
        return (f'** {x}have been added to your meal :) **')
    else:
                   return "You do not order yet !!"

if __name__=="__main__":
    print(a)
    order=input("> ")
    total_order=[]
    x="" 
    while order!="quit":
        total_order=order_fun(x)
        order=input("> ")
    
    print(f'***********************************')        
    print(total(x,order))
    print(f'***********************************')   