# Generated by Django 4.2 on 2024-02-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_qunatity_cartdetail_quantity_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='HUGNI9OJ', max_length=10),
        ),
    ]
