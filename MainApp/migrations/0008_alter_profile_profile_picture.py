# Generated by Django 4.1.1 on 2023-05-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='C:/Users/Ricky/Desktop/ExpertOpinion/ExpertOpinion/images/good_pic_vI22z3e.png'),
        ),
    ]
