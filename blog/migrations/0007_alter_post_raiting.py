# Generated by Django 3.2.4 on 2021-06-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='raiting',
            field=models.IntegerField(default=0),
        ),
    ]
