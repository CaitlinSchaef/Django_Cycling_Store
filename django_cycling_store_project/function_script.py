import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_cycling_store_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from django_cycling_store_app.models import *
import builder_script
#python function_script.py  

# Do all of these functions then need a class? Like a CreatedOrder Class that produces order objects?
# def order_create_function():
#     // need to delete the vehicle from stock
#     print()

# def order_view_function():
#     //
#     print()

# def order_update_function():
#     //
#     print()

# def order_delete_function():
#     //
#     print()

# def employee_portal():
    #print('Welcome to the Employee Portal!')
    #print('Would you like to delete an existing order, create a new order, view an existing order, update an existing order, or order more stock?')
    #select_question = input (f'Select 1 to delete an existing order, Select 2 to create a new order, Select 3 to view an existing order, Select 4 to update an existing order, Select 5 to order more stock.')
     
# def customer_portal():
    #print('Welcome to the Customer Portal!')
    #print('Would you like to create a new order, view an existing order, or update an existing order?')
    #select_question = input (f'Select 1 to create a new order, Select 2 to view an existing order, Select 3 to update an existing order.')


def greeting_function():
    main_question = input (f'Are you an employee or customer? Select 1 for Customer OR Select 2 for Employee.')
    if main_question == "1":
       print('Opening Customer Portal...')
    #    customer_portal()
    elif main_question == "2":
       print('Opening Customer Portal...')
    #    employee_portal()
    else:
       print('That is not an option!')
       greeting_function()

    

def display_function():
    print("Hello! Welcome to the Django Cycling Shop!")
    greeting_function()
    # order_create_function()
    # order_view_function()
    # order_update_function()
    # order_delete_function()

display_function()