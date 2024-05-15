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

# vehicle = Vehicle.objects.get(type='big wheel')
# object_list = CustomerOrder.objects.bulk_create(
#     [
#         CustomerOrder(date_month=4, date_day=20, date_year=2023, vehicle=vehicle),
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

unicycle = Vehicle.objects.filter(type='unicycle')
bicycle = Vehicle.objects.filter(type='bicycle')
tricycle = Vehicle.objects.filter(type='tricycle')

customer_orders = CustomerOrder.objects.all()

unicycle.customer_order_set.add(customer_orders[0])
bicycle.customer_order_set.add(customer_orders[1])
tricycle.customer_order_set.add(customer_orders[2])
unicycle.customer_order_set.add(customer_orders[3])
customer_orders.save()

# do something like this for when you're making an order
# list = [unicycle, bicycle]
# order = CustomerOrder(date=1, vehicles=list)
# order.save()