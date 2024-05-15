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