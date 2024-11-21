# Generated by Django 5.1.1 on 2024-11-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('in stock', 'в наличии'), ('issued', 'выдана')], max_length=9),
        ),
    ]
