# Generated by Django 4.1.1 on 2023-07-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Poll',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='question',
            new_name='title',
        ),
    ]
