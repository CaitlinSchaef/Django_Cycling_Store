from django.db import models

                ## Create your models here. ##

# python manage.py makemigrations 
# python manage.py migrate

class Vehicle(models.Model):
    type = models.TextField(max_length=50, default='bicycle', null=True)
    number_in_stock = models.PositiveIntegerField(default=0, null=True)
    price = models.PositiveIntegerField(default=3500, null=True)
    color = models.TextField(max_length=50, default='black', null=True)

    def __str__(self):
        return f'Type: {self.type}, Price: ${self.number_in_stock}, Color: {self.color}, Number In Stock: {self.number_in_stock}'

class Customer(models.Model):
    name = models.CharField(max_length=75, null=True)

    def __str__(self):
        return f'Customer Name: {self.name}'

class CustomerOrder(models.Model):
    date_month = models.PositiveIntegerField(4)
    date_day = models.PositiveIntegerField(12)
    date_year = models.PositiveIntegerField(2024)
    customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_date = '{date_month}-{date_day}-{date_year}'
    paid = models.TextField(null=True, default='not paid')

    def __str__(self):
        return f'ORDER: Customer Name:{self.customer_name}, Customer Order: {self.order}, Order Date: {self.created_date}, Paid: {self.paid} '

