# Generated by Django 4.2.8 on 2024-01-11 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_books_account_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='account_balance',
        ),
    ]