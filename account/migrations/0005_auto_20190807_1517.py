# Generated by Django 2.0.2 on 2019-08-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='dob',
            field=models.CharField(default='05-05-1996', max_length=100),
        ),
        migrations.AddField(
            model_name='visitor_perma',
            name='dob',
            field=models.CharField(default='05-05-1996', max_length=100),
        ),
        migrations.AlterField(
            model_name='temp',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]