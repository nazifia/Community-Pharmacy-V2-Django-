# Generated by Django 5.1.5 on 2025-01-19 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('store', '0006_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='sales',
            name='wholesale_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.wholesalecustomer'),
        ),
    ]
