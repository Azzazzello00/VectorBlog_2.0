# Generated by Django 2.2.4 on 2021-04-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eblog', '0006_auto_20210426_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='', max_length=200),
        ),
    ]
