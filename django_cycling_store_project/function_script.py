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
     
# def customer_portal():


def greeting_function():
    main_question = input (f'Are you an employee or customer? Select 1 for Customer OR Select 2 for Employee.')
    if main_question != 1 or main_question != 2:
       print('That is not an option!')
       greeting_function()
    elif main_question == "1":
       print('Opening Customer Portal...')
    #    customer_portal()
    elif main_question == "2":
       print('Opening Customer Portal...')
    #    employee_portal()
    else:
       print('WHY AM I HERE IT BROKE')

    

def display_function():
    print("Hello! Welcome to the Django Cycling Shop!")
    greeting_function()
    # order_create_function()
    # order_view_function()
    # order_update_function()
    # order_delete_function()

display_function()