# Generated by Django 4.1.1 on 2022-10-30 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_alter_products_category_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('reservation_id', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='Order #')),
                ('reservation_date', models.DateTimeField()),
                ('number_of_guests', models.IntegerField()),
                ('reserved', models.BooleanField(default=True)),
                ('check_in', models.BooleanField(default=False)),
                ('table_number', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='product',
        ),
        migrations.DeleteModel(
            name='CustomerOrder',
        ),
        migrations.DeleteModel(
            name='OrderProducts',
        ),
    ]