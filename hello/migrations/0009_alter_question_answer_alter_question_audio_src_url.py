# Generated by Django 4.1.3 on 2022-11-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_alter_question_audio_src_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='audio_src_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
