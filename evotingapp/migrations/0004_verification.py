# Generated by Django 4.0.1 on 2022-03-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evotingapp', '0003_voterids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(max_length=13)),
                ('aadharnumber', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'verification',
            },
        ),
    ]
