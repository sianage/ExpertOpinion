# Generated by Django 4.1.1 on 2023-07-04 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_rename_question_poll_rename_question_choice_poll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.poll'),
        ),
    ]
