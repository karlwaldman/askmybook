# Generated by Django 4.1.3 on 2022-11-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_alter_question_answer_alter_question_audio_src_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='real_answer',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
