# Generated by Django 4.0.5 on 2022-07-07 18:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_task2_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task2',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('04faf468-5e2a-42a6-9e69-194be431a23b'), editable=False, primary_key=True, serialize=False),
        ),
    ]