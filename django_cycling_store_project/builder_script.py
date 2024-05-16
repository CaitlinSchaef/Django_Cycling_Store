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
#python builder_script.py  

#############################################################################################################################################################################
#Created vehicle 

# object_list = Vehicle.objects.bulk_create(
#     [
#         Vehicle(type='bicycle', color='green', number_in_stock=10, price=250),
#         Vehicle(type='unicycle', number_in_stock=9, price=150),
#         Vehicle(type='tricycle', color='blue', number_in_stock=20, price=300)
#     ]
# )

# vehicles = Vehicle.objects.all()
# for vehicle in vehicles:
#     print(vehicle)

#############################################################################################################################################################################
#Created customers

# object_list = Customer.objects.bulk_create(
#     [
#         Customer(name='Millie Bobby Brown'),
#         Customer(name='Henry Cavill'),
#         Customer(name='Jim Tater'),
#         Customer(name='Marcus Schaeffer'),
#     ]
# )

# customers = Customer.objects.all()
# for customer in customers:
#     print(customer)

#############################################################################################################################################################################
#Creating CustomerOrder (just gave dates)
# vehicle = Vehicle.objects.get(type='big wheel')
# object_list = CustomerOrder.objects.bulk_create(
#     [
#         CustomerOrder(date_month=4, date_day=20, date_year=2023 vehicle=vehicle),
#         CustomerOrder(date_month=7, date_day=22, date_year=2024,),
#     ]
# )

# customer_orders = CustomerOrder.objects.all()
# for customer_order in customer_orders:
#     print(customer_order)


# customer_order = CustomerOrder.objects.get(id=2)

# customer_order.customer_name = Customer.objects.get(name='Millie Bobby Brown')

# customer_order.save()


# customer_orders = CustomerOrder.objects.all()
# for i in customer_orders:
#     print(i)

##################################
#Updated CustomerOrders: 

# filtering the vehicles by type
# unicycle = Vehicle.objects.filter(type='unicycle').first()
# bicycle = Vehicle.objects.filter(type='bicycle').first()
# tricycle = Vehicle.objects.filter(type='tricycle').first()

# #calling all customer orders
# customer_orders = CustomerOrder.objects.all()

# # for order in customer_orders:
# #     print(f"ORDER: {order.customer_name} is here")

# #telling what vehicle to attach to specific customer orders
# unicycle.order.add(customer_orders[0])
# # unicycle.vehicles_in_order_set.add(customer_orders[0])
# bicycle.order.add(customer_orders[1])
# tricycle.order.add(customer_orders[2])
# unicycle.order.add(customer_orders[3])
# # customer_orders.save()

# #saving those updates
# unicycle.save()
# tricycle.save()
# bicycle.save()


#these printed all by vehicle type
# print(unicycle)
# for order in unicycle.order.all():
#     print("\n *****************")
#     print(f"\n \n{order}")
#     for v in order.vehicles_in_order.all():
#         print(f"\n \t {v}")

# for order in bicycle.order.all():
#     print("\n *****************")
#     print(f"\n \n{order}")
#     for v in order.vehicles_in_order.all():
#         print(f"\n \t {v}")

# for order in tricycle.order.all():
#     print("\n *****************")
#     print(f"\n \n{order}")
#     for v in order.vehicles_in_order.all():
#         print(f"\n \t {v}")

# #this is going to display all orders, need to think about maybe displaying by customer?
# def disp_orders(vech_type):
#     for order in vech_type.order.all():
#         print("\n *****************")
#         print(f"\n \n{order}")
#     for v in order.vehicles_in_order.all():
#         print(f"\n \t {v}")

# #calling this function and passing bicycle as a parameter prints just the orders that have bicycles
# disp_orders(bicycle)

# do something like this for when you're making an order
# list = [unicycle, bicycle]
# order = CustomerOrder(date=1, vehicles=list)
# order.save()