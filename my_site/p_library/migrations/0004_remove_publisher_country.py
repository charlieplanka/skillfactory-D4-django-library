# Generated by Django 2.2.6 on 2020-11-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20201126_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='country',
        ),
    ]
