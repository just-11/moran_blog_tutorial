# Generated by Django 2.2 on 2023-01-03 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20230103_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='colume',
            new_name='column',
        ),
    ]
