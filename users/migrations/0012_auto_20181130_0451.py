# Generated by Django 2.1.3 on 2018-11-30 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20181130_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='id',
            new_name='user_id',
        ),
    ]
