# Generated by Django 4.1.1 on 2022-09-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0003_futebol_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='futebol',
            name='publicacao',
            field=models.BooleanField(default=False),
        ),
    ]
