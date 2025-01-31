# Generated by Django 5.1.5 on 2025-01-19 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_itemselectionhistory_wholesaleselectionhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesitem',
            name='dosage_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.formulation'),
        ),
        migrations.AddField(
            model_name='wholesalesalesitem',
            name='dosage_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.formulation'),
        ),
    ]
