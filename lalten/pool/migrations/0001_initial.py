# Generated by Django 4.2.3 on 2023-09-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ninja',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]