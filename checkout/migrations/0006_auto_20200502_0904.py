# Generated by Django 2.2.12 on 2020-05-02 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200427_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='subscription',
            field=models.ForeignKey(default='No longer available', on_delete=django.db.models.deletion.SET_DEFAULT, to='products.Subscription'),
        ),
    ]
