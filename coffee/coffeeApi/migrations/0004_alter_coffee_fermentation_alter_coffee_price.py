# Generated by Django 4.0.2 on 2022-02-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApi', '0003_alter_coffee_farm_alter_coffee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='fermentation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]