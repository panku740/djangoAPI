# Generated by Django 4.0.5 on 2022-07-07 18:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task2_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task2',
            name='id',
        ),
        migrations.AddField(
            model_name='task2',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('2dab4550-03c3-4df1-8037-05d993403772'), editable=False, primary_key=True, serialize=False),
        ),
    ]
