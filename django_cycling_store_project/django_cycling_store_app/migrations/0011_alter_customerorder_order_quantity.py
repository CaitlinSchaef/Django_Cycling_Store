# Generated by Django 5.0.6 on 2024-05-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cycling_store_app', '0010_customerorder_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]