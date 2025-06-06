# Generated by Django 5.2.1 on 2025-05-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0004_products_delete_familymemb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
            ],
        ),
    ]
