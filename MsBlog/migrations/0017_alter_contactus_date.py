# Generated by Django 3.2 on 2021-04-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MsBlog', '0016_auto_20210430_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Contact Date'),
        ),
    ]
