# Generated by Django 5.1.6 on 2025-02-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_productmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
