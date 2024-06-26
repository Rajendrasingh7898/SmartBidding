# Generated by Django 4.1.4 on 2023-02-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('ptitle', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('baseprice', models.IntegerField()),
                ('pdescription', models.CharField(max_length=1000)),
                ('uid', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=50)),
            ],
        ),
    ]
