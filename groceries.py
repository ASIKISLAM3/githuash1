from datetime import datetime
# User data class
class Userdata:
    users = []
    def __init__(self,user_id:int,user_name:str,mail_id:str,password:str,phone_no:str):
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.password = password
        self.phone_no = phone_no
# User Functionality class
class User_Functionality:
    def user_validation(self,email,password = None):
        registered_mail_id = [user.mail_id for user in Userdata.users if user.mail_id == email]
        
        if not registered_mail_id and password==None:
            return True 
        else:
            verified_password = [user.password for user in Userdata.users if user.password == password]
            if registered_mail_id and verified_password :
                return True
        
    def signup(self):
        user_id = (Userdata.users[-1].user_id)+1
        user_name = input("Enter your name : ").title()
        mail_id = input("Enter your email : ").lower()
        password = input("Enter your password : ").lower()
        phone_no = input("Enter your phone no : ")
        
        if self.user_validation(mail_id):
            new_user = Userdata(user_id,user_name,mail_id,password,phone_no)
            Userdata.users.append(new_user)
            return mail_id
        
    def login(self):
        input_email = input("Enter your registered mail id : ").lower()
        input_password = input("Enter your password : ").lower()
        mail_id = input_email
        if self.user_validation(input_email,input_password):
            return mail_id
        
# GroceryCategory data class
class Grocery_category_data:
    categories = []
    def __init__(self,category_id:int,category_name:str):
        self.category_id = category_id
        self.category_name = category_name
        
# Grocery data class
class Grocery_data:
    fruits = []
    vegetables = []
    snacks = []
    def __init__(self,grocery_id : int,grocery_name : str,quantity : str,cost : int):
        self.grocery_id = grocery_id
        self.grocery_name = grocery_name
        self.quantity = quantity
        self.cost = cost

# Grocery_System_Functionality
class Grocery_functionality:
    def category_display(self):
        print("--------------------------------------------------------\n")
        for category in Grocery_category_data.categories:
            print(category.category_id," ",category.category_name)
            
    def select_category(self):
        category_id = int(input("Please enter the category id : "))
        for category in Grocery_category_data.categories:
            if category.category_id == category_id:
                return category.category_name,category.category_id
            
    def fruits_display(self):
        print("--------------------------------------------------------\n")
        for fruit in Grocery_data.fruits:
            print(fruit.grocery_id," ",fruit.grocery_name," ",fruit.quantity," ",fruit.cost)
            
    def select_fruit(self):
        fruit_id = int(input("Enter the fruit id : "))
        for fruit in Grocery_data.fruits:
            if fruit.grocery_id == fruit_id:
                return fruit.grocery_name,fruit_id
    
    def vegetables_display(self):
        print("--------------------------------------------------------\n")
        for vegetable in Grocery_data.vegetables:
            print(vegetable.grocery_id," ",vegetable.grocery_name," ",vegetable.quantity," ",vegetable.cost)
    
    def select_vegetable(self):
        vegetable_id = int(input("Enter the vegetable id : "))
        for vegetable in Grocery_data.vegetables:
            if vegetable.grocery_id == vegetable_id:
                return vegetable.grocery_name,vegetable_id
            
    def snack_display(self):
        print("--------------------------------------------------------\n")
        for snack in Grocery_data.snacks:
            print(snack.grocery_id," ",snack.grocery_name," ",snack.quantity," ",snack.cost)
            
    def select_snack(self):
        snack_id = int(input("Enter the snack id : "))
        for snack in Grocery_data.snacks:
            if snack.grocery_id == snack_id:
                return snack.grocery_name,snack_id
#Booking Data
class BookingData:
    orders = []
    def __init__(self,mail_id,selected_category,selected_item,total_cost,payment_mode,order_placed_time):
        self.mail_id = mail_id
        self.category = selected_category
        self.item = selected_item
        self.price = total_cost
        self.payment_mode = payment_mode
        self.order_placed_time = order_placed_time
        
# Booking Functionality
class Booking_functionality:
    def order_preview(self,mail_id,selected_category,selected_item,total_cost):
        print("--------------------------------------------------------\n")
        print("Booking Preview:\n")
        print(f'Category Name: {selected_category}')
        print(f'Grocery Name: {selected_item}')
        print(f'Total Price: {total_cost}')
        print("--------------------------------------------------------\n")
        payment_choice = int(input("Payment Options:\n1. Card\n2. UPI : "))
        print("--------------------------------------------------------\n")
        if payment_choice != 1 and payment_choice != 2:
            print("Invalid Payment method")
            return False
        
        else:
            if payment_choice == 1:
                payment_mode = "Card"
                print("Booked Successfully")
            elif payment_choice == 2:
                payment_mode = "UPI"
                print("Booked Successfully")
            order_placed_time = datetime.now().strftime("%y/%m/%d,%H:%M:%S")
            new_order = BookingData(mail_id,selected_category,selected_item,total_cost,payment_mode,order_placed_time)
            BookingData.orders.append(new_order)
            return True
        
    def order_history(self):
        if len(BookingData.orders)==0:
            print("Booking history is empty...")
        else:
            print("--------------------------------------------------------\n")
            for history in BookingData.orders:
                print(history.mail_id,history.category,history.item,history.price,history.payment_mode,history.order_placed_time,sep = "__")
    
    def delete_history(self):
         if len(BookingData.orders) == 0:
            print("Booking history is empty.")
         else:
            del(BookingData.orders[-1])
            print("Your last history has been deleted")
            choice = input("\nDo you clear your all history? (y/n):\n")
            if choice.lower() ==  'y':
                BookingData.orders.clear()
                print("Booking history deleted successfully")
            else:
                print("Invalid input.")
    
# Booking system class
class Grocery_Booking_System:
    def __init__(self):
        self.user = User_Functionality()
        self.grocery = Grocery_functionality()
        self.order = Booking_functionality()
        self.stay_in = True 
        self.mail_id = None
    
    def signup_or_login(self):
        choice = input("Enter your choice \n Signup/Login : ").title()
        if choice=="Signup":
            self.mail_id = self.user.signup()
            if not self.mail_id :
                print("Exisiting user")
                self.stay_in = False
        elif choice=="Login":
            self.mail_id = self.user.login()
            if not self.mail_id :
                print("Invalid mail or password")
                self.stay_in = False
                
                
    def run(self):
        while self.stay_in:
            print("--------------------------------------------------------\n")
            print("Main Menu:")
            print("1. Order Grocery")
            print("2. Display Order history")
            print("3. Delete Order history")
            print("4. Logout")
            choice = int(input("\nEnter your choice:\n"))
            if choice==1:
                self.order_grocery()
            elif choice==2:
                self.display_order_history()
            elif choice==3:
                self.delete_order_history()
            elif choice==4:
                self.logout()
            else:
                print("Invalid Choice.......")
                return
            
    def order_grocery(self):
        total_cost = 0
        self.grocery.category_display()
        selected_category,choice = self.grocery.select_category()
        selected_item = ""
        if choice==1:
            self.grocery.fruits_display()
            seleted_item,choice = self.grocery.select_fruit()
            if not seleted_item:
                print("Invalid choice")
            else:
                count = int(input("How much you want to buy : "))
                total_cost = count*(Grocery_data.fruits[choice-1].cost)
                
        elif choice==2:
            self.grocery.vegetables_display()
            seleted_item,choice = self.grocery.select_vegetable()
            if not seleted_item:
                print("Invalid choice")
            else:
                count = int(input("How much you want to buy : "))
                total_cost = count*(Grocery_data.vegetables[choice-1].cost)
        elif choice==3:
            self.grocery.snack_display()
            selected_item,choice = self.grocery.select_snack()
            if not selected_item:
                print("Invalid choice")
            else:
                count = int(input("How much you want to buy : "))
                total_cost = count*(Grocery_data.snacks[choice-1].cost)
        else:
            print("Invalid Category Id...")
            return
        if not self.order.order_preview(self.mail_id,selected_category,selected_item,total_cost):
            self.stay_in = False
            
    def display_order_history(self):
        self.order.order_history()
            
    def delete_order_history(self):
        self.order.delete_history()
    
    def logout(self):
        print("Logged out successfully......")
        self.stay_in = False
        return
if __name__ == '__main__':
    user1 = Userdata(1,"Bakiya","bakiya123@gmail.com","bakiya123","6745127412")
    user2 = Userdata(2,"Dinesh","dinesh321@gmail.com","dinesh321","7451368411")
    user3 = Userdata(3,"Indhu","indhun2004@gmail.com","indhu2004","3238465831")
    Userdata.users.append(user1)
    Userdata.users.append(user2)
    Userdata.users.append(user3)
    
    category1 = Grocery_category_data(1,"Fruits")
    category2 = Grocery_category_data(2,"Vegetables")
    category3 = Grocery_category_data(3,"Snacks items")
    Grocery_category_data.categories.append(category1)
    Grocery_category_data.categories.append(category2)
    Grocery_category_data.categories.append(category3)
    
    fruit1 = Grocery_data(1,"Apple","1 kg",100)
    fruit2 = Grocery_data(2,"Orange","1 kg",80)
    fruit3 = Grocery_data(3,"Grape","1 kg",120)
    fruit4 = Grocery_data(4,"Mango","1 kg",50)
    Grocery_data.fruits.append(fruit1)
    Grocery_data.fruits.append(fruit2)
    Grocery_data.fruits.append(fruit3)
    Grocery_data.fruits.append(fruit4)
    
    vegetable1 = Grocery_data(1,"Potato","1 kg",40)
    vegetable2 = Grocery_data(2,"Onion","1 kg",30)
    vegetable3 = Grocery_data(3,"Brinjal","1 kg",25)
    vegetable4 = Grocery_data(4,"Carat","1 kg",40)
    Grocery_data.vegetables.append(vegetable1)
    Grocery_data.vegetables.append(vegetable2)
    Grocery_data.vegetables.append(vegetable3)
    Grocery_data.vegetables.append(vegetable4)
    
    snack1 = Grocery_data(1,"Biscuit","1 Packet",30)
    snack2 = Grocery_data(2,"Sweet","1 kg",100)
    snack3 = Grocery_data(3,"Chocolate","1 Packet",50)
    Grocery_data.snacks.append(snack1)
    Grocery_data.snacks.append(snack2)
    Grocery_data.snacks.append(snack3)
    
    booking_system = Grocery_Booking_System()
    booking_system.signup_or_login()
    booking_system.run()
