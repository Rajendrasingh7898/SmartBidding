# Generated by Django 4.1.4 on 2023-02-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('txnid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('info', models.CharField(max_length=50)),
            ],
        ),
    ]
