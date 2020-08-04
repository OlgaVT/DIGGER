# Generated by Django 2.2.13 on 2020-08-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('pfam_id', models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
