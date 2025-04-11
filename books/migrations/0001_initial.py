# Generated by Django 5.1.4 on 2025-03-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('edition', models.CharField(max_length=15)),
                ('price', models.FloatField()),
            ],
        ),
    ]
