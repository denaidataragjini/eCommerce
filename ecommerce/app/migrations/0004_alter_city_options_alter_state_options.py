# Generated by Django 5.0.4 on 2024-05-28 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_city_state_customer_city_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
    ]