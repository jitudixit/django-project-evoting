# Generated by Django 4.0.1 on 2022-03-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evotingapp', '0002_regdetails_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoterIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voterid', models.CharField(max_length=5)),
                ('issuedate', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'voterids',
            },
        ),
    ]