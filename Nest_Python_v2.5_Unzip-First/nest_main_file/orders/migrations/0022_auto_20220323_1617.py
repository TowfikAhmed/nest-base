# Generated by Django 3.2.12 on 2022-03-23 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_alter_product_prdslug'),
        ('orders', '0021_ordersupplier_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailssupplier',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderdetailssupplier',
            name='order_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.ordersupplier'),
        ),
        migrations.AlterField(
            model_name='orderdetailssupplier',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AlterField(
            model_name='ordersupplier',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order'),
        ),
    ]
