# Generated by Django 5.1.2 on 2024-11-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='description',
            field=models.TextField(),
        ),
    ]
