# Generated by Django 4.1.1 on 2022-09-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createcontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('nickName', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField(max_length=11)),
                ('workno', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('birthday', models.DateField(max_length=100)),
                ('anniversary', models.DateField(max_length=100)),
                ('hstreet', models.CharField(max_length=100)),
                ('hcity', models.CharField(max_length=100)),
                ('hstate', models.CharField(max_length=100)),
                ('hcountry', models.CharField(max_length=100)),
                ('hpostcode', models.CharField(max_length=100)),
                ('wstreet', models.CharField(max_length=100)),
                ('wcity', models.CharField(max_length=100)),
                ('wstate', models.CharField(max_length=100)),
                ('wcountry', models.CharField(max_length=100)),
                ('wpostcode', models.CharField(max_length=100)),
            ],
        ),
    ]
