# Generated by Django 4.1.3 on 2022-11-04 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.AddField(
            model_name='question',
            name='ask_count',
            field=models.IntegerField(default=0),
        ),
    ]
