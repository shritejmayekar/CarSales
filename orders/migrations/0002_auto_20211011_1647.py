# Generated by Django 3.2.8 on 2021-10-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
