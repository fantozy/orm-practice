# Generated by Django 5.1.2 on 2024-10-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(null=True),
        ),
    ]
