# Generated by Django 4.1.7 on 2023-02-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_order_total_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=65, null=True, verbose_name='Total'),
        ),
    ]