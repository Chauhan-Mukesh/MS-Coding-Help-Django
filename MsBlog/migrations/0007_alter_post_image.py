# Generated by Django 3.2 on 2021-04-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MsBlog', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thumb_uploads/', verbose_name='Post Image'),
        ),
    ]
