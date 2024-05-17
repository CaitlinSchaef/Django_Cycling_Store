import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_cycling_store_project.settings"
django.setup()
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW
#############################################################################################################################################################################
from django_cycling_store_app.models import *
import builder_script
#python function_script.py  
#############################################################################################################################################################################

    # customer_orders = CustomerOrder.objects.all()
#   date_month = models.PositiveIntegerField(default=4)
#     date_day = models.PositiveIntegerField(default=12)
#     date_year = models.PositiveIntegerField(default=2024)
#     customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     vehicles_in_order = models.ManyToManyField(Vehicle, related_name='order') #type, price, color
#     order_quantity = models.PositiveIntegerField(default=1)
#     paid = models.TextField(null=True, default='not paid')
#############################################################################################################################################################################
def create_customer_function():
    print('Create a new customer:')
    new_customer_name = input(f'Enter customer name for the order now:\t')
    return Customer.objects.create(name=new_customer_name)
    
    
    
#Order to create an order:
def order_create_function():
    ###### Calling create customer function(), because the customer has to exist to add to order :(
    print('Are you a new customer?')
    customer_question = input(f'Yes/No\t')
    name = ''
    if customer_question == "Yes":
        name = create_customer_function()
    else:
        customer_order_name = input(f'Enter name:\t')
        name = Customer.objects.filter(name=customer_order_name).first()
        if bool(~name):
            return order_create_function()
    ############################################################################################################
    ######## Selecting vehicle for order
    print('What would you like to order?')
    vehicle_question = input(f'Select 1 for unicycle, \nSelect 2 for bicycle,\n Select 3 for tricycle\t')
    if vehicle_question.isnumeric():
        vehicle_question = int(vehicle_question)
    else:
        print('That is not an option')
        order_create_function()
    
    if vehicle_question == 1:
        vehicle_type = 'unicycle'
    elif vehicle_question == 2:
        vehicle_type = 'bicycle'
    elif vehicle_question == 3:
        vehicle_type = 'tricycle'
    else:
        print('That is not an option')
    
     # we need to identify what vehicle record we are working with
    vehicle = Vehicle.objects.filter(type=vehicle_type).first()
    ###################################################################################################################
    #######Selecting number of vehicles
    print('How many {vehicle_type}s would you like?')
    quantity_question = input(f'Enter quantity to purchase:\t')
    if quantity_question.isnumeric():
        quantity_question = int(quantity_question)
    else:
        print('That is not an option.')
    
    if quantity_question <= vehicle.number_in_stock:
        quantity = quantity_question
    else:
        print('Sorry, this vehicle is out of stock!')
    
    ###################################################################################################################
    ###########Input date:
    print('What is the order date?')
    month_input = int(input(f'Month: #\t'))
    day_input = int(input(f'Day: #\t'))
    year_input = int(input(f'Year: ####\t'))

    if month_input > 12 or month_input < 1:
        print('That is not a valid month.')
    else:
        month = month_input
    
    if day_input > 31 or day_input < 1:
        print('That is not a valid day.')
    else:
        day = day_input

    if year_input > 2025 or year_input < 1999:
        print('That is not a valid year.')
    else:
        year = year_input
    
    ###################################################################################################################
    ############ Checking for payment:

    print('How much would you like to pay today?')
    payment_input = int(input(f'Enter amount: \t'))

    commerce = 'not paid'
    if payment_input == vehicle.price:
        commerce = 'paid'
    
    
    
    new_order = CustomerOrder.objects.create(customer_name=name, order_quantity=quantity, date_month=month, date_day=day, date_year=year, paid=commerce)
    # we need to identify what vehicle record we are working with
    #  vehicle = Vehicle.objects.filter(type=vehicle_type).first()
    # add that vehicle record to this order - 
    order = new_order
    order.vehicles_in_order.add(vehicle) #or should this be new_order = 
    # save the order again - 
    new_order.save()
    # subtract the quantity from vehicle.number_in_stock
    vehicle.number_in_stock - new_order.order_quantity
    # save vehicle
    vehicle.save()
    print(new_order)



def order_view_function():
    print('Look up order by name:')
    order_name = input(f'Enter name on order:\t')
    customer = Customer.objects.filter(name=order_name)
    for custy in customer:
        print(f'{custy.id} - {custy.name}')
    chosen_custy = input(f'Select ID of Account: \t')
    customer = Customer.objects.get(id=chosen_custy)
    print(customer.id, customer)
    # pulled_order = CustomerOrder.objects.filter(customer_name=customer.id)
    current_customer = None
    # print(pulled_order)
    for order in customer.customerorder_set.all():
        print(f'ID: {order.id}, {order}')

# def order_update_function():
#     //
#     print()

def order_delete_function():
    all_customers = Customer.objects.all()
    all_orders = CustomerOrder.objects.all()
    print('Hello employee! Would you like to delete a Customer or delete an Order?')
    deletion_selection = input(f'Select 1 to delete Customer, \nSelect 2 to delete Order. ')
    if deletion_selection.isnumeric():
        deletion_selection = int(deletion_selection)
    else:
        print('That is not an option.')
    
    if deletion_selection == 1:
        print('You have selected "Delete Customer"...')
        print(all_customers)
        deletion_customer_options = input(f'Look up customer by ID or by Name. \nSelect 1 for ID, Select 2 for Name: \t')
        if deletion_customer_options.isnumeric():
            deletion_customer_options = int(deletion_customer_options)
        else:
            print('That is not an option.')
            order_delete_function()
        
        if deletion_customer_options == 1:
            customer_deletion_by_id = input(f'Enter customer ID:\t ')
            delete_by_id = Customer.objects.get(id=customer_deletion_by_id)
            delete_by_id.delete()
            print('Customer deleted.')
            print(all_customers)
        elif deletion_customer_options == 2:
            customer_deletion_by_name = input(f'Enter customer name as it appears in records:\t ')
            delete_by_name = Customer.objects.get(name=customer_deletion_by_name)
            delete_by_name.delete()
            print('Customer deleted.')
            print(all_customers)
        else:
            print('That is not an option.')
            order_delete_function()
    elif deletion_selection == 2:
        print('You have selected "Delete Order"...')
        print(all_orders)
        deletion_order_options = input(f'Look up order by Order ID or by Customer Name:\n Select 1 for Order ID,\n Select 2 for Customer Name: \t ')
        if deletion_order_options.isnumeric():
            deletion_order_options = int(deletion_order_options)
        else:
            print('That is not an option.')
            order_delete_function()

        if deletion_order_options == 1:
            order_deletion_by_id  = input(f'Enter order ID:\t')
            if order_deletion_by_id.isnumeric():
                order_deletion_by_id = int(order_deletion_by_id)
                delete_order_by_id = CustomerOrder.objects.get(id=order_deletion_by_id)
                delete_order_by_id.delete()
                print('Order deleted.')
                print(all_orders)
            else:
                print('That is not an ID.')
                order_delete_function()
        elif deletion_order_options == 2:
            order_deletion_by_name = input(f'Enter customer name as it appears with order:\t')
            delete_order_by_name = CustomerOrder.objects.get(customer_name=order_deletion_by_name)
            delete_order_by_name.delete()
            print('Order deleted.')
            print(all_orders)
        else:
            print('That is not an option.')  
    else:
        print('That is not an option')

#############################################################################################################################################################################
#This is the employee portal
def employee_portal():
    print('Welcome to the Employee Portal!')
    print('Would you like to delete an existing order or customer, create a new order, view an existing order, update an existing order, or order more stock?')
    select_question = input (f'Select 1 to delete an existing order or customer,\n Select 2 to create a new order,\n Select 3 to view an existing order,\n Select 4 to update an existing order,\n Select 5 to order more stock.')
    if select_question.isnumeric():
        select_question = int(select_question)
    else:
        print('That is not an option')
        employee_portal()
    
    if select_question == 1:
        print('Opening delete functionality...')
        order_delete_function()
    elif select_question == 2:
        print('Creating a new order... ')
        order_create_function()
    elif select_question == 3:
        order_view_function()
    else:
        print('That is not an option.')
#############################################################################################################################################################################
#This is the customer portal
   
def customer_portal():
    print('Welcome to the Customer Portal!')
    print('Would you like to create a new order, view an existing order, or update an existing order?')
    select_question = input (f'Select 1 to create a new order, \nSelect 2 to view an existing order,\nSelect 3 to update an existing order.\n')
    if select_question.isnumeric():
        select_question = int(select_question)
    else:
        print('That is not an option')
        customer_portal()
    
    if select_question == 1:
        print('Creating new order...')
        order_create_function()
    elif select_question == 2:
        print('Pulling existing orders...')
        order_view_function()
    elif select_question == 3:
        print('Pulling existing orders to update...')
        #order_update_function()
    else:
        print('That is not an option')
        customer_portal()

#############################################################################################################################################################################
#This is the greeting/select function to choose which portal

def greeting_function():
    main_question = input (f'Are you an employee or customer? \n\tSelect 1 for Customer \n\tSelect 2 for Employee.')

    if main_question == "1":
       print('Opening Customer Portal...')
       customer_portal()
    elif main_question == "2":
       print('Opening Employee Portal...')
       employee_portal()
    else:
       print('That is not an option!')
       greeting_function()

#############################################################################################################################################################################
######### This is the only function we will actually call on the page, I suppose we could get rid of it and just use the greeting function.

def display_function():
    print("Hello! Welcome to the Django Cycling Shop!")
    greeting_function()
    

# for custy in Customer.objects.filter(name="Molly Ringwald"):
#     print(custy.id, custy)
display_function()