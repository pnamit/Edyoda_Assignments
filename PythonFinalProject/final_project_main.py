import csv
import re
from datetime import date,time, datetime

class ZippyFoodmain:
    def __init__(self):
        pass

#--------------- Admin Login---------------------------------------------

# This method accepts the password from an admin user and continues to admin options after validation
# reads the file adminpwd.txt for comparing the password

    def admin_login():
        # print("we are in admin login")
        existing_pwd=""
        with open("adminpwd.txt",'r') as pwd_file:
            existing_pwd=pwd_file.read()
        admin_pwd=""
        admin_home_page_flag=True
        while (admin_pwd.upper() != "Q" and admin_home_page_flag==True):    
            # print("---------------Administrator Login-----------------------")
            # print("---------------------------------------------------------")
            # print("    ")
            admin_pwd = input(f"Enter Password (or enter 'Q' to quit) : ")
            if admin_pwd==existing_pwd: 
                print("    ")
                print("You have logged in successfully! ") 
                ZippyFoodmain.admin_options()
                admin_home_page_flag=False
            elif admin_pwd.upper()=='Q':
                print("quitting")
            else:
                print("invalid password")
                continue
        return

#--------------- Admin Options --------------------------------------------

# This method displays the options for the admin user and accepts the choice
# calls the method based on the option chosen
# also provides an option to quit to the main menu
# 

    def admin_options():        
        # print("we are in admin options")
        admin_option_input=""
        press_key_list_admin = {"A": "Add Menu Items", 
                                "D": "Display Menu Items", 
                                "M":"Modify Menu Items", 
                                "C":"Change Password",
                                "Q": "Quit"}        
        while not (admin_option_input.upper() == "Q"):
            print("---------------------------------------------------------")    
            print("               Administrator options  ")
            print("---------------------------------------------------------")
            for key, value in press_key_list_admin.items():
                print("Press", key, "To", value)
            admin_option_input = input("\nPress Key : ").upper()
            if admin_option_input == "A":
                
                # print("\n admin_add_menu_items()\n")
                ZippyFoodmain.admin_add_item()
            elif admin_option_input == "D":
                # print("into fod display option")
                ZippyFoodmain.admin_display_menu_items()
            elif admin_option_input == "M":
                ZippyFoodmain.admin_modify_item()
            elif admin_option_input == "C":
                # print("\nadmin_change_pwdn")
                ZippyFoodmain.admin_change_pwd()

            elif admin_option_input == "Q":
                print("\nHave a nice day!\n")
            else:
                print(" ")         
                print("Invalid Entry, try again!")
                print(" ")
                continue   

#--------------- Admin Display Item List---------------------------------------------

# This method is accessed by the admin user to display the list of food items available in the 
# restaurant with its details
# reads the data from foodmaster.csv and displays 

    def admin_display_menu_items():
        print("------------------------------------------------------------------------------")
        print("    Food Items List  ")
        print("------------------------------------------------------------------------------")
        print("Food","  Name",'\t','\t',"  Pack of",'\t'," On the","  Price","  Discount","  Avlbl")
        print("ID  ","      ",'\t','\t',"         ",'\t'," menu  ","       ","          ","  Stock")
        print("------------------------------------------------------------------------------")

        with open("foodmaster.csv") as foodmaster_r:
            foodmaster_dictreader = csv.DictReader(foodmaster_r) 
            for line in foodmaster_dictreader:
                print(f'{line.get("food_id"):7}{line.get("food_name"):20}{line.get("food_desc_units"):15}{line.get("food_on_the_menu"):9}{line.get("food_price"):8}{line.get("food_discount")}%\t      {line.get("food_avlbl_stock")}')    

        print("------------------------------------------------------------------------------")


#--------------- Admin Add Item---------------------------------------------

# This methods is accessed by the admin user to add new food items to the menu
# uses the data from foodmaster to validate and write the new data row into it
# data entry uses the static methods of validation

    def admin_add_item():

        # print("inside func")

        with open("foodmaster.csv") as foodmaster_r:
            foodmaster_dictreader = csv.DictReader(foodmaster_r) 
            food_master_add_list =[]
            for line in foodmaster_dictreader:
                food_master_add_list.append(line["food_id"])

        # print(food_master_add_list)

        food_master_add_dict={}
        add_food_id_flag='Y'
        while add_food_id_flag=='Y':
            
            # add_food_id=input("Enter Food_iD or Q to exit : ")
            print("")
            add_food_id=z.regex_validate_q('^[A-Z]{2}[0-9]{2}$',"Food Id (2 alphabets+2 digits) or Q to quit")
            if add_food_id.upper()=='Q':
                return
            elif add_food_id in food_master_add_list:
                print(" Food Id already exists")
            else:
                food_master_add_dict["food_id"]=add_food_id
                # food_master_add_dict["food_name"]=input("Enter Food Name ")
                food_master_add_dict["food_name"]=z.gen_string_validate(15,"Food Name (max 15 characters)")
                # food_master_add_dict["food_desc_units"]=input("Enter Food Units (pieces/grams/inches,etc.) ")
                food_master_add_dict["food_desc_units"]=z.gen_string_validate(15,"Food Units (pieces/grams/inches,etc.) (max 15 characters)")
                # food_master_add_dict["food_on_the_menu"]=input("Enter Availability (Y/N) ")
                food_master_add_dict["food_on_the_menu"]=z.yn_validate("Enter Availability (Y/N) ")
                # food_master_add_dict["food_price"]=input("Enter Food Price ")
                food_master_add_dict["food_price"]=z.int_validate(0,9999,"valid Food Price ")

                # food_master_add_dict["food_discount"]=input("Enter Discount % ")
                food_master_add_dict["food_discount"]=z.int_validate(-1,100," Discount % ")
                # food_master_add_dict["food_avlbl_stock"]=input("Enter Stock Qty available ")
                food_master_add_dict["food_avlbl_stock"]=z.int_validate(-1,1000," Stock Qty ")

                add_food_id_flag='N'

                # print(food_master_add_dict)
                # print(food_master_add_dict.values())

        with open("foodmaster.csv",'a', newline='') as foodmaster_w: 
            field_headers = ["food_id","food_name","food_desc_units","food_on_the_menu","food_price","food_discount","food_avlbl_stock"]
            csv_writer=csv.DictWriter(foodmaster_w,fieldnames=field_headers)
            # csv_writer.writeheader() # add this if header is required to be written
            # csv_writer.writerow({"food_id":"FO06",
            #                     "food_name":"2",
            #                     "food_desc_units":"2",
            #                     "food_on_the_menu":"2",
            #                     "food_price":"2",
            #                     "food_discount":"2","food_avlbl_stock":"2"})
            # print("after file opening",food_master_add_dict)
            # for x in food_master_add_dict:
            #     print(x)
            csv_writer.writerow(food_master_add_dict)

        return

#--------------- Admin Modify Item---------------------------------------------

# in this method the admin user can modify the items on the menu in the restaurant
# accesses the foodmaster.csv file and updates it with the changed values
# uses static methods for data entry validations 

# The 'available on the menu' option is used to withdraw items from the menu or bring them back 
# there is no option to delete the item. It is being retained to maintain data integrity with 
# the customer's order history

    def admin_modify_item():
        with open("foodmaster.csv") as foodmaster_r:
            foodmaster_dictreader = csv.DictReader(foodmaster_r) 
            foodmaster_dict={}
            for line in foodmaster_dictreader:
                foodmaster_dict.update({line["food_id"]:line})

        print ("---------------------------------------")
        print ("Available menu items for modification :")
        print ("---------------------------------------")
        for key,values in foodmaster_dict.items():
            print(foodmaster_dict[key]["food_id"], foodmaster_dict[key]["food_name"]) 

        foodid_to_be_modified=""

        while foodid_to_be_modified not in (foodmaster_dict.keys()):
            foodid_to_be_modified=input(f"\nEnter food id to be modified : ")
            print("")
            if foodid_to_be_modified in (foodmaster_dict.keys()):
                # available_on_menu=input(f"Is this still available on the menu (Y/N?): ")
                available_on_menu=z.yn_validate("Is this still available on the menu (Y/N?) ")
                print(f'Current Price : {foodmaster_dict[foodid_to_be_modified]["food_price"]} ',end=" , ")
                # new_price=input(f"Enter price : ")
                new_price=z.int_validate(0,9999,"New valid Food Price ")
                # new_discount=input(f"Enter discount : ")
                print(f'Current Discount % : {foodmaster_dict[foodid_to_be_modified]["food_discount"]} ',end=" , ")
                new_discount=z.int_validate(-1,100,"New Discount % ")
                # new_stock_qty=input(f"Enter current stock available : ")
                print(f'Current Stock : {foodmaster_dict[foodid_to_be_modified]["food_avlbl_stock"]} ',end=" , ")
                new_stock_qty=z.int_validate(-1,1000,"New Stock Qty ")
            else:
                print("Food Id not available. Try again")
                continue

        foodmaster_dict[foodid_to_be_modified]["food_on_the_menu"]=available_on_menu
        foodmaster_dict[foodid_to_be_modified]["food_price"]=new_price
        foodmaster_dict[foodid_to_be_modified]["food_discount"]=new_discount
        foodmaster_dict[foodid_to_be_modified]["food_avlbl_stock"]=new_stock_qty

        # for key,values in foodmaster_dict.items():
        #     print(key,values)

        with open("foodmaster.csv",'w', newline='') as foodmaster_w: 
            field_headers = ["food_id","food_name","food_desc_units","food_on_the_menu","food_price","food_discount","food_avlbl_stock"]
            csv_writer=csv.DictWriter(foodmaster_w,fieldnames=field_headers)
            csv_writer.writeheader() # add this if header is required to be written
            for x in foodmaster_dict.values():
                # print(x)
                csv_writer.writerow(x)

#--------------- Admin Password Change ---------------------------------------------

# this method is invoked by the admin user when the change password option is chosen
# accepts the new password and write into adminpwd.txt 

    def admin_change_pwd():
        # print("we are in admin change password")
        print("")
        new_pwd=z.regex_validate('^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]){8}$',"new alpha-numeric 8 digit password ")

        
        # with open("pwd.txt",'r') as pwd_file:
        #     existing_pwd=pwd_file.read()
        
        with open("adminpwd.txt",'w',newline='') as pwd_file:
            pwd_file.write(new_pwd)
            
        return

#--------------- Customer Login---------------------------------------------
# this method is accessed by the customer to login using his 10 digit mobile number as the customer id
# and a 6 digit numeric pin as his password 
# his id/pwd details are validated from the cust_profile.csv file
# post login the customer is redirected to the customer options method 

# is he is a new user - he has an option to register and invokes the customer registration method


    def customer_login():
        # print("we are in customer login")
        cust_profile_dict={}

        with open("cust_profile.csv") as csv_r:
            csv_dictreader = csv.DictReader(csv_r)
            for line in csv_dictreader:
                cust_profile_dict.update({line["cust_id"]:line})

        cust_id_list=[]
        for key in cust_profile_dict:
            cust_id_list.append(key)

        customer_home_flag=True
        customer_id=""            
        customer_pwd=""
        # customer_id = input(f"Enter 10-digit mobile number (or enter 'Q' to quit) : ")
        customer_id = z.int_validate_q(999999999,10000000000,"valid 10 digit mobile no ")
        if customer_id=="Q":
            # print("quitting before login")
            return
        elif customer_id not in cust_id_list:
            
            cust_register_flag=input("\nYou are a new customer! Do you want to register now ? (Y/N)  ")
            if cust_register_flag.upper()=='Y':
                z.customer_register(customer_id)
                return                
        else:            
            while (customer_pwd.upper() != "Q" and customer_home_flag==True):    
                # customer_pwd = input(f"Enter Password (or enter 'Q' to quit) : ")
                customer_pwd = z.int_validate_q(99999,1000000,"valid 6 digit password ")
                if customer_pwd.upper()=='Q':
                    print("")
                                    
                else:
                    for data in cust_profile_dict:
                        if data==customer_id:
                            if cust_profile_dict[customer_id]["cust_pwd"]==customer_pwd:
                                # print("success match")
                                z.customer_options(customer_id)
                                customer_home_flag=False
                                return
                            else:
                                # print("password invalid after file read")
                                continue
                            
            return
             


#--------------- Customer Options---------------------------------------------

# this method displays all the options available for the customer post login
# based on the choice, the respective methods are invoked

    def customer_options(self,cust_id):  
        self.cust_id=cust_id      
        # print("we are in customer options")
        # print(cust_id)
        customer_option_input=""
        press_key_list_customer =   {"O": "Order Food",
                                     "H": "View Order History", 
                                     "P": "View/Edit Profile",
                                     "Q": "Quit"}


        while not (customer_option_input.upper() == "Q"):    
            print("---------------------------------------------------------")
            print("                  Customer options   ")
            print("---------------------------------------------------------")
            for key, value in press_key_list_customer.items():
                print("Press", key, "To", value)
            customer_option_input = input("\nPress Key : ").upper()
            if customer_option_input == "O":
                # print("\n customer_order_food()\n")
                z.customer_order_food(cust_id)
            elif customer_option_input == "H":
                # print("\n customer_order_history()\n")
                z.customer_order_history(cust_id)
            elif customer_option_input == "P":
                z.customer_profile_edit(cust_id)
            elif customer_option_input == "Q":
                print("Have a nice day!")
            else:
                print(" ")         
                print("Invalid Entry, try again!")
                print(" ")
                continue   

#--------------- Customer Register---------------------------------------------

# this method is invoked when a new customer chooses to register
# this methods collects the password and other profile details of the customer and 
# stores the data in cust_profile.csv
# invokes static validation methods during data entry


    def customer_register(self,cust_id):
        self.cust_id=cust_id
        # self.cust_pwd=cust.pwd
        print("----------------------------------------")
        print("Thank you for choosing Zippy Foods!")
        print("----------------------------------------")
        print(f"Your registered mobile number is {cust_id}")
        print("")
        # cust_pwd=input("Please choose a 6-digit password :")
        cust_pwd=z.int_validate(99999,1000000,"a valid 6 digit password ")
        # print(cust_id, cust_pwd)
        print("")
        print("Please provide more details about yourself")
        print("")
        # cust_name=input("Please enter Full Name (max 30 characters): ")
        cust_name=z.regex_validate('^[a-zA-Z][a-zA-Z ]{1,24}$',"Please enter Full Name (max 25 characters)")
        # cust_email=input("Please enter email_id (max 50 characters) :  ")
        cust_email=z.regex_validate('^(?=.{1,25}$)([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$',"valid email id  ")
        # cust_pincode=input("Please enter valid 6 digit pincode :  ")
        cust_pincode=z.int_validate(99999,1000000,"valid 6 digit pincode ")
        # cust_address=input("Please enter address (max 100 characters) : ")
        cust_address=z.gen_string_validate(100,"address(max 100 characters)")
        
        print(cust_name,cust_email,cust_address,cust_pincode)


        with open("cust_profile.csv",'a',newline='') as csv_w:
            csv_writer=csv.writer(csv_w)
            csv_writer.writerow([cust_id,cust_pwd,cust_name,cust_email,cust_pincode,cust_address])
        print("registered successfully" )
        print("Please login again to order food!")
        return               
        
#--------------- Customer Order Food---------------------------------------------

# this method allows the customer to place an order from the restaurant
# displays the available food items and accepts the food id and qty for ordering
# validates the food item and the qty against what is available
# accepts multiple food items as part of the order.

# displays availability from the foodmaster.csv file
# calculates the offer price based on the discount data in foodmaster.csv 

# post ordering updates the foodmaster.csv file with the revised stock quantity based on the order qty

# also adds the customer order details in the cust_ord_history.csv file
# adds into history with the data and time of placing the order
# calculates the amount paid for each item using the discounted price of the item 

# invokes static validation methods during data entry


    def customer_order_food(self,cust_id):
        self.cust_id=cust_id
        # print("into cust order food")
        # print(cust_id)
        # print ("available food")
        # print("Name",'\t','\t',"Pack of",'\t',"Available",'\t',"MRP",'\t',"Offer Price",'\t')
                
        cust_order_dict={}

        print("---------------------------------------------------------------------")
        print("Food  ","Name",'\t','\t',"Pack of",'\t',"MRP",'\t',"Offer",'\t',"Avlbl")
        print("ID  ", "    ",'\t','\t',"       ",'\t',"   ",'\t',"Price",'\t',"Stock")
        print("---------------------------------------------------------------------")

        with open("foodmaster.csv") as foodmaster_r:
                    foodmaster_dictreader = csv.DictReader(foodmaster_r) 
                    for line in foodmaster_dictreader:
                        if line.get("food_on_the_menu")=='Y':
                            print(line.get("food_id"),"",
                            line.get("food_name"),'\t',
                            line.get("food_desc_units"),'\t',
                            line.get("food_price"),'\t',
                            int((int(line.get("food_price"))*(100-int(line.get("food_discount"))))/100),'\t',
                            ("Not Available" if int(line.get("food_avlbl_stock"))==0 else "Available")
                            )
                        else:
                            continue

        print("---------------------------------------------------------------------")      

# a='FO01'
# b=10
        with open("foodmaster.csv") as foodmaster_r:
                    foodmaster_dictreader = csv.DictReader(foodmaster_r) 
                    cust_order_dict={}
                    for line in foodmaster_dictreader:
                        if line.get("food_on_the_menu")=='Y':
                            cust_order_dict.update({line["food_id"]:line})
                        else:
                            continue
                    # print(cust_order_dict)
                    # print(cust_order_dict.values())

        order_list=[]
        cust_ord_hist_dict={}
        cust_ord_hist_dict_line={}

        #ord_date=date_time.strftime("%Y-%b-%d,%I:%M %p")

        order_completion_flag=''
        new_order_qty=0
        while order_completion_flag!='N':
            new_order_id=""
            while new_order_id not in cust_order_dict or int(cust_order_dict[new_order_id]["food_avlbl_stock"])==0:
                new_order_id=input("Enter Food ID for the item you need to order : ")     
                if new_order_id not in cust_order_dict or int(cust_order_dict[new_order_id]["food_avlbl_stock"])==0:
                    print("Invalid Food Id or Food ID not available today, enter again")
                else:
                    continue
    # print(new_order_qty)
    # print(int(cust_order_dict[new_order_id]["food_avlbl_stock"]))
    
            new_order_qty_flag=''
            while new_order_qty_flag!='Y':
            # while new_order_qty < int(cust_order_dict[new_order_id]["food_avlbl_stock"]): 
                new_order_qty=int(input("Enter order quantity : "))
                if new_order_qty > int(cust_order_dict[new_order_id]["food_avlbl_stock"]):
                        print("Required quantity not available, enter again")
                else:
                    # print("required qty satisfied")
                    new_order_qty_flag='Y'

            cust_ord_hist_dict_line={}
            date_time=datetime.now()
            # print(date_time.strftime("%Y-%b-%d,%I:%M:%S:%f %p"))
            order_list.append([new_order_id,new_order_qty])
            cust_ord_hist_dict_line['ord_date']=date_time.strftime("%Y-%b-%d,%I:%M:%S %p")
            cust_ord_hist_dict_line['cust_id']=cust_id
            cust_ord_hist_dict_line['food_id']=new_order_id
            cust_ord_hist_dict_line['food_name']=cust_order_dict[new_order_id]["food_name"]
            cust_ord_hist_dict_line['ord_qty']=new_order_qty
            cust_ord_hist_dict_line['amt_paid']=new_order_qty*int((int(cust_order_dict[new_order_id]["food_price"])*(100-int(cust_order_dict[new_order_id]["food_discount"])))/100)

            if new_order_qty > 0:
                cust_ord_hist_dict.update({cust_ord_hist_dict_line["ord_date"]:cust_ord_hist_dict_line})

    # new_order_qty*int((int(cust_order_dict["food_price"])*(100-int(cust_order_dict["food_discount"])))/100)
    
            # print(cust_ord_hist_dict_line)
            # print(cust_ord_hist_dict)

        # ord_date,cust_id,food_id,food_name,ord_qty,amt_paid

            # print(cust_order_dict[new_order_id]["food_avlbl_stock"]), 
            # print(new_order_qty)
            cust_order_dict[new_order_id]["food_avlbl_stock"]=int(cust_order_dict[new_order_id]["food_avlbl_stock"])-int(new_order_qty)
            # print(cust_order_dict[new_order_id]["food_avlbl_stock"])
            

            order_completion_flag=z.yn_validate("Do you need to order more (Y/N) ? ")
            if order_completion_flag=='Y':
                continue
            else:
                with open("foodmaster.csv",'w', newline='') as foodmaster_w: 
                    field_headers = ["food_id","food_name","food_desc_units","food_on_the_menu","food_price","food_discount","food_avlbl_stock"]
                    csv_writer=csv.DictWriter(foodmaster_w,fieldnames=field_headers)
                    csv_writer.writeheader() # add this if header is required to be written
                    for x in cust_order_dict.values():
                        # print(x)
                        csv_writer.writerow(x)

                print("")
                print("Your Order is successful !")
                order_completion_flag='N'



        with open("cust_ord_history.csv",'a', newline='') as cust_ord_history_a: 
            field_headers =['ord_date','cust_id','food_id','food_name','ord_qty','amt_paid']
            csv_writer=csv.DictWriter(cust_ord_history_a,fieldnames=field_headers)
        #   csv_writer.writeheader() # add this if header is required to be written
            for x in cust_ord_hist_dict.values():
                # print(x)
                csv_writer.writerow(x)

        return

#--------------- Customer View Order History---------------------------------------------

# This method displays the customers order history 

# fetches the data from the file cust_ord_history.csv


    def customer_order_history(self,cust_id):
        self.cust_id=cust_id
        print("")
        print("Your Order History")
        # print(cust_id)

        print("---------------------------------------------------------------------")
        print("Order Date","\t",'\t',"Food","\t","Name",'\t',"      Ord","   Amt")
        print("          ","\t",'\t',"ID  ","\t","    ",'\t',"      Qty","   Paid")
        print("---------------------------------------------------------------------")

        cust_hist_flag=""
        with open("cust_ord_history.csv") as cust_ord_history_r:
            cust_ord_history_dictreader = csv.DictReader(cust_ord_history_r)
                    # ord_date,cust_id,food_id,food_name,ord_qty,amt_paid 


            for line in cust_ord_history_dictreader:
                if line.get("cust_id")==cust_id:
                    cust_hist_flag='Y'
                    print (f'{line.get("ord_date"):25}{line.get("food_id"):7}{line.get("food_name"):15}{line.get("ord_qty"):7}{line.get("amt_paid")}')

            if cust_hist_flag!='Y':
                print("You have not placed any orders yet!")

        return

#--------------- Customer Profile Edit---------------------------------------------

# This method allows the customer to edit his profile 

# displays the existing details and allows to edit the specifc detail based on his choice

# accesses the file cust_profile.csv to display and then write into with the updated details

# invokes static validation methods during data entry



    def customer_profile_edit(self,cust_id):
        self.cust_id=cust_id
        # self.cust_id=cust_id
        # print("inside profile edit")
        
        cust_profile_dict={}

        with open("cust_profile.csv") as csv_r:
            csv_dictreader = csv.DictReader(csv_r)
            for line in csv_dictreader:
                cust_profile_dict.update({line["cust_id"]:line})
        
        
        print("Your existing details")

        print("Mobile No        : ",cust_profile_dict[cust_id]["cust_id"])
        print("Current Password : ",cust_profile_dict[cust_id]["cust_pwd"])
        print("Current Name     : ",cust_profile_dict[cust_id]["cust_name"])
        print("Current Email    : ",cust_profile_dict[cust_id]["cust_email"])
        print("Current Pincode  : ",cust_profile_dict[cust_id]["cust_pincode"])
        print("Current Address  : ",cust_profile_dict[cust_id]["cust_address"])
        print(" ")
        # print(len(cust_profile_dict))
        # print(cust_id)
        # print(cust_profile_dict[cust_id]["cust_name"])
        
        print("What would you like to edit ?")
        cust_profile_edit_options_dict={'1':'Password','2':'Name','3':'Email','4':'Pincode','5':'Address','Q':'Quit'}
        # print(cust_profile_edit_options_dict)
        # print(cust_profile_edit_options_dict.keys())
        # print(cust_profile_edit_options_dict.keys)

        cust_prof_edit_option=""
        # print(cust_id)

        for key, value in cust_profile_edit_options_dict.items():
            print("Press", key, "To edit", value)
        
        while cust_prof_edit_option not in cust_profile_edit_options_dict.keys():
            cust_prof_edit_option = input("Press Key : ").upper()
            if cust_prof_edit_option not in cust_profile_edit_options_dict.keys():
                print("Invalid entry")

        
        if cust_prof_edit_option=="1":
            # print("1:password")
            # new_pwd=input("Enter changed password : ")
            # cust_profile_dict[cust_id]["cust_pwd"]=input("Enter changed password : ")
            cust_profile_dict[cust_id]["cust_pwd"]=z.int_validate(99999,1000000,"valid 6 digit password ")
        elif cust_prof_edit_option=="2":
            # print("2:name")
            # print("inside option 2",cust_id)
            # print(cust_profile_dict[cust_id]["cust_name"])
            # new_name=input("Enter changed name : ")
            # cust_profile_dict[cust_id]["cust_name"]=new_name
            # cust_profile_dict[cust_id]["cust_name"]=input("Enter changed name : ")
            cust_profile_dict[cust_id]["cust_name"]=z.regex_validate('^[a-zA-Z][a-zA-Z ]{1,24}$',"Please enter Full Name (max 25 characters):")
        elif cust_prof_edit_option=="3":
            # print("3:email")
            # new_email=input("Enter changed email : ")
            # cust_profile_dict[cust_id]["cust_email"]=input("Enter changed email : ")
            cust_profile_dict[cust_id]["cust_email"]=z.regex_validate('^(?=.{1,25}$)([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$',"valid email id  ")
                
        elif cust_prof_edit_option=="4":
            # print("4:pincode")
            # new_pincode=input("Enter changed pincode : ")
            # cust_profile_dict[cust_id]["cust_pincode"]=input("Enter changed pincode : ")
            cust_profile_dict[cust_id]["cust_pincode"]=z.int_validate(99999,1000000,"valid 6 digit pincode ")
        elif cust_prof_edit_option=="5":
            # print("5:address")
            # new_address=input("Enter changed address : ")
            # cust_profile_dict[cust_id]["cust_address"]=input("Enter changed address : ")
            cust_profile_dict[cust_id]["cust_address"]=z.gen_string_validate(100,"changed address(max 100 characters)")
    
        elif cust_prof_edit_option.upper()=="Q":
            return

        # print(cust_prof_edit_option)
        # print(new_pwd,new_name,new_email,new_pincode,new_address)
        
        # print(cust_profile_dict)


        # cust_id,cust_pwd,cust_name,cust_email,cust_pincode,cust_address
        # print(cust_profile_dict)
        # print(len(cust_profile_dict))
        # test_dict={}
        # counter_x=0
        with open("cust_profile.csv",'w',newline="") as custmaster_edit_w: 
            field_headers = ["cust_id","cust_pwd","cust_name","cust_email","cust_pincode","cust_address"]
            csv_writer=csv.DictWriter(custmaster_edit_w,fieldnames=field_headers)
            csv_writer.writeheader() # add this if header is required to be written
            # for x in cust_profile_dict.values():
            #     test_dict.update(x)
            #     counter_x+=1
            #     csv_writer.writerow(x)
            for x in cust_profile_dict.values():
                # counter_x+=1
                csv_writer.writerow(x)
                # print("Inside for loop",cust_profile_dict[x])
                #csv_writer.writerows(cust_profile_dict)


        # print(test_dict)
        # print(len(test_dict))
        # print(counter_x)
        return

#--------------- Home Page ---------------------------------------------

# this method is the login home page of the restuarant on which a customer or admin user can login
# based on the option chosen invokes the respective method



    def home_page():

        press_key_list_main =  {"C": "Order Food", 
                                "A": "Login as Administrator",
                                "Q": "Quit"}
# press_key_list_admin = {"A": "Add Menu Items", "D": "Display Menu Items", "M":"Modify Menu Items", "C":"Change Password","Q": "Quit"}
# press_key_list_customer = {"O": "Order Food", "H": "Order History", "P":"View/Edit Profile","Q": "Quit"}

        home_key_press = False

        while not (home_key_press == "q"): 
            print(f"-------------------------------------------")
            print(f"      Welcome to Zippy Foods!              ")
            print(f"-------------------------------------------")
            for key, value in press_key_list_main.items():
                print("Press", key, "To", value)
            home_key_press = input("\nPress Key : ").upper()
            if home_key_press == "C":
                print("\n         Welcome Customer!\n")
                ZippyFoodmain.customer_login()
            elif home_key_press == "A":
                print("\n Welcome Administrator !\n")
                ZippyFoodmain.admin_login()
            elif home_key_press == "Q":
                print("\nWe hope to see you again, have a nice day!\n")
                break
            else:
                print(" ")         
                print("Invalid Entry, try again!")
                print(" ")
            continue   

#--------------- static methods ---------------------------------------------

# these are static methods used to validate user inputs either as numeric, or string 
# and uses regex in some of them to match specific patterns

# these methods are called by other methods with the required arguments

    @staticmethod
    def int_validate(min_value,max_value,print_string):

        valid_flag='N'
        while valid_flag=='N':
            # print(min_value)
            # print(max_value)
            output=input(f'Enter {print_string} : ')
            # print(output.isnumeric)
            if output.isnumeric()==True and int(output) > min_value and int(output) < max_value :
                valid_flag='Y'
                return(output)
            else:
                print("Invalid entry")


    @staticmethod
    def int_validate_q(min_value,max_value,print_string):

        valid_flag='N'
        while valid_flag=='N':
            # print(min_value)
            # print(max_value)
            output=input(f'Enter {print_string} or Q to quit : ')
            # print(output.isnumeric)
            if output.upper()=='Q':
                return('Q')
            
            elif output.isnumeric()==True and int(output) > min_value and int(output) < max_value :
                valid_flag='Y'
                return(output)
            else:
                print("Invalid entry")

    @staticmethod
    def gen_string_validate(field_length,print_string):
        valid_flag='N'
        while valid_flag=='N':
            output=input(f'Enter {print_string}: ')
            if len(output)==0:
                print("field cannot be blank")
            elif len(output)>field_length:
                print("length exceeded")
            else:
                valid_flag='Y'
                return(output)

    @staticmethod
    def gen_string_validate_q(field_length,print_string):
        valid_flag='N'
        while valid_flag=='N':
            output=input(f'Enter {print_string} : ')
            if output.upper()=='Q':
                return('Q')
            elif len(output)>field_length:
                print("length exceeded")
            else:
                valid_flag='Y'
                return(output)

    @staticmethod
    def yn_validate(print_string):
        valid_flag='N'
        while valid_flag=='N':
            output=input(f'{print_string} : ')
            if output=='Y' or output=='N':
                valid_flag=='Y'
                return(output.upper())
                
            else:
                print("Invalid Entry")
            
    
    @staticmethod
    def regex_validate(regex_string,print_string):
        valid_flag='N'
        while valid_flag=='N':
            output=""
            output_entry=input(f'Enter {print_string}: ')
            # print(re.match(regex_string,output))
            if re.match(regex_string,output_entry):
                # print("match")
                output=output_entry
                valid_flag='Y'
                re.purge()
                return(output)            
            else:
                re.purge()
                print("Invalid entry")

    @staticmethod
    def regex_validate_q(regex_string,print_string):
        valid_flag='N'
        while valid_flag=='N':
            output=""
            output_entry=input(f'Enter {print_string} : ')
            if output_entry.upper()=='Q':
                return('Q')
            elif re.match(regex_string,output_entry):
                # print(re.match(regex_string,output))
                # print("match")
                output=output_entry
                valid_flag='Y'
                re.purge()
                return(output)            
            else:
                re.purge()
                print("Invalid entry")

#--------------- Call here---------------------------------------------
# the program is invoked here

z=ZippyFoodmain()
ZippyFoodmain.home_page()

#--------------- End of Program---------------------------------------------

