# Generated by Django 5.0.6 on 2024-05-15 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cycling_store_app', '0005_alter_vehicle_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_cycling_store_app.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_in_stock',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.PositiveIntegerField(default=3500, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.TextField(default='bicycle', max_length=50, null=True),
        ),
    ]
