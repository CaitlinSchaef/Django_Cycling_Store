# Generated by Django 5.0.6 on 2024-05-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cycling_store_app', '0002_customerorder_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='paid',
            field=models.TextField(default='not paid', null=True),
        ),
    ]