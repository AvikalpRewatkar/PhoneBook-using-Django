# Generated by Django 4.1.1 on 2022-11-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_createcontact_bloodgroup_alter_createcontact_phoneno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcontact',
            name='anniversary',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='createcontact',
            name='birthday',
            field=models.CharField(max_length=100),
        ),
    ]
