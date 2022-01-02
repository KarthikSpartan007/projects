#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Food_App():
    def __init__(self):
        self.Food_menu={}
        self.User_details={}
        self.order=[]
    def LogIn(self):
        while True:
            S=input("Log In as \n 1.Admin\n 2.Customer\n 3.Exit\n")
            if S=="1":
                enter=input("Enter choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="1":
                    print(self.add_food())
                    enter=input("Enter choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="2":
                    print(self.edit_food())
                    enter=input("Enter choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="3":
                    print(self.list_of_food())
                    enter=input("Enter choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="4":
                    print(self.remove_food())
                    enter=input("Enter choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                else:
                    pass
            elif S=='2':
                choice=input("Enter Choice\n 1.Register\n 2.signin\n")
                if choice=="1":
                    print(self.REgistration())
                    choice=input("Enter Choice\n 1.Register\n 2.signin\n") 
                if choice=="2":
                    print(self.signin())
                    choice=input("Enter Choice\n 1.Register\n 2.signin\n")
                else:
                    print("Thank You")
                    break
            else:
                print("wrong option")
                break
    def add_food(self):
        variable=input("Do you want to add food (Y/N): ").lower()
        while True:
            if variable=="y":
                try:
                    foods=input("Enter the name of food: ")
                    quantity=(input("Enter the Quantity of food: ")+" Piece")
                    price=int(input("Enter the price of food: "))
                    stock=int(input("Enter the stock of food: "))
                    self.id=len(self.Food_menu)+1
                    self.Food_menu[self.id]={"Food name":foods,"qty":quantity,"price":price,"stock":stock}
                    variable=input("Do you want to add food (Y/N): ")
                except KeyError:
                    print("Key Error")
            else:
                print("Thank you")
                break
    def edit_food(self):
        var=input("Do you want to edit food (Y/N): ").lower()
        if var=='y':
            print("Press 1 to see the food list")
            print("Press 2 to quit")
            n=int(input("Enter your choice:  "))
            if n==1:
                print("Food list\n",self.Food_menu)
                v=int(input("Enter the food id if want to edit: "))
                k=int(input("Enter the option which you want to edit\n 1.Food name\n 2.qty\n 3.price\n 4.Edit whole items\n 0.exit\n"))
                if k==1:
                    print(self.Food_menu[v])
                    b=input("Enter the food name you want to edit: ")
                    self.Food_menu[v]["Food name"]=b
                    print( self.Food_menu)
                elif k==2:
                    print(self.Food_menu[v])
                    a=input("Enter the food Stock you want to edit: ")
                    self.Food_menu[v]["stock"]=a
                    print(self.Food_menu)
                elif k==3:
                    print(self.Food_menu[v])
                    c=input("Enter the food Price you want to edit: ")
                    self.Food_menu[v]["price"]=c
                    print(self.Food_menu)
                elif k==4:
                    print(self.Food_menu[v])
                    b=input("Enter the food name you want to edit: ")
                    a=input("Enter the food Stock you want to edit: ")
                    c=input("Enter the food Price you want to edit: ")
                    self.Food_menu[v]["Food name"]=b
                    self.Food_menu[v]["stock"]=a
                    self.Food_menu[v]["price"]=c
                    print(self.Food_menu)
                elif k==0:
                    print("Thank You")
            elif n==2:
                 print("Thank You")
                
    def remove_food(self):
        print(self.Food_menu)
        delete=int(input("Enter the food id you want to delete:  "))
        self.Food_menu.pop(delete)
        print(self.Food_menu)
    def list_of_food(self):
        for i in self.Food_menu:
            print("Food Name: ",self.Food_menu[i]["Food name"])
            print("Quantity : ",self.Food_menu[i]["qty"])
            print("Price    : ",self.Food_menu[i]["price"])
    def REgistration(self):
        print("Register on the Application : ")
        self.user_data={}
        Full_Name=input("Enter your full name :")
        Phone_No=input("Enter your phone number :")
        Email=input("Enter your email : ")
        Address=input("Enter your address :")
        Password=input("Enter your password :")
        print("\nYou have registered successfully.")
        self.user_data["Name"]=Full_Name
        self.user_data["Mobile"]=Phone_No
        self.user_data["Mail"]=Email
        self.user_data["Address"]=Address
        self.user_data["Password"]=Password
        self.user_name=Full_Name+"$"
        self.User_details[self.user_name]=self.user_data
        print("User Name: ",self.user_name)
        
#         self.User_details.append(self.user_data)
    def signin(self):
        print("From here you can log in.")
        while True:
            Full_Name=input("\nEnter your Name for login : ")
            Password=input("Enter your passward :")
            if self.user_data["Name"]==Full_Name:
                if self.user_data["Password"]==Password:
                    print("\nlogin successfull")
                    while True:
                        user_input=int(input("\nPlease enter your preference :\n 1.Place New Order\n 2.order history\n 3.update profile\n 4.exit\n :\n ENter your choice :"))
                        if user_input==1:
                            print("\nplease select your preference from below list : ")
                            #show food list
                            self.show_foodlist()
                        elif user_input==2:
                            print("Here is your Order History \n")
                            self.order_history()
                        elif user_input==3:
                            self.update_profile()
                        else:
                            print("Thank You")
                            break
                    else:
                        break
                else:
                    break
        else:
            print("\nPlease enter correct name and password.")

        
    def show_foodlist(self):
#         print(self.Food_menu)
        food_list=[]
        for i in self.Food_menu:
            food_list.append(self.Food_menu[i])
        print("\nHere is the food list.")
        for i in food_list:
            print(f"{food_list.index(i)+1}. {i['Food name']} ({i['qty']}) [INR {i['price']}]")

        while True:
            user_choice=input("\nif you want to choOse any item enter yes else no:")
            if user_choice=="yes":
                user_input=int(input("\nPlease select your choice by the number of the food :"))
                print("\nHere is your selected order : ",food_list[(user_input-1)])
                items=food_list[(user_input-1)]
                self.order.append(items)
            
            else:
                break      
        print("\nHere is your complete items list :",self.order)
        confirmation=(input("\nDo you want to PLace the order:\n 1.yes\n 2.no\n "))
        if confirmation=="yes":
            print("\nyour order is placed.")
        else:
            print("\nyour order is canceled.")
            pass
    def update_profile(self):
#         print(self.User_details)
        var=input("Do you want to edit food (Y/N): \n").lower()
        if var=='y':
            print("Press 1 to see the Profile\n")
            print("Press 2 to quit\n")
        n=input("Enter your choice:  \n")
        if n=="1":
            print("Profile\n",self.User_details)
            v=input("Enter the User Name if want to edit: \n")
            for i in self.User_details:
                j=i
                while v==j:
                    k=int(input("Enter the option which you want to edit\n 1.Name\n 2.Mobile Number\n 3.Mail \n 4.Address\n 5.Edit Entire Profile \n 0.exit\n"))
                    if k==1:
                        print(self.User_details)
                        b=input("Enter the 'NAME' you want to edit: \n")
                        self.User_details[v]["Name"]=b
                        print(self.User_details)
                    elif k==2:
                        print(self.User_details[v])
                        a=input("Enter the 'MOBILE NUMBER' you want to edit: ")
                        self.User_details[v]["Mobile"]=a
                        print(self.User_details)
                    elif k==3:
                        print(self.User_details[v])
                        c=input("Enter the 'MAIL' you want to edit: \n")
                        self.User_details[v]["Mail"]=c
                        print(self.User_details)
                    elif k==4:
                        print(self.User_details[v])
                        d=input("Enter the 'Address' you want to edit: \n")
                        self.User_details[v]["Address"]=d
                        print(self.User_details)
                    elif k==5:
                        print(self.User_details[v])
                        b=input("Enter the 'NAME' you want to edit: \n")
                        a=input("Enter the 'MOBILE NUMBER' you want to edit: \n")
                        c=input("Enter the 'MAIL' you want to edit: \n")
                        d=input("Enter the 'Address' you want to edit: \n")
                        self.User_details[v]["Name"]=b
                        self.User_details[v]["Mobile"]=a
                        self.User_details[v]["Mail"]=c
                        self.User_details[v]["Address"]=d
                        print(self.User_details)
                    elif k==0:
                        print("Thank You")
                        break
        elif n==2:
            print("Thank You")
        else:
            print("Wrong id")
            v=input("Enter the name id if want to edit: ")
        
    def order_history(self):
        for i in self.order:
                print(f"{self.order.index(i)+1}. {i['Food name']} ({i['qty']}) [INR {i['price']}]")
        



                
    
                    
                    


# In[10]:


a=Food_App()


# In[ ]:


a.LogIn()


# In[ ]:




