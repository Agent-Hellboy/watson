# Generated by Django 3.1.4 on 2020-12-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_task_freq_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='urls',
            field=models.JSONField(default=list),
        ),
    ]