# Generated by Django 4.1.1 on 2023-07-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_debate_author_debate_opponent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='field',
            new_name='academic_field',
        ),
    ]