# Generated by Django 2.1.2 on 2018-10-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('author', models.CharField(max_length=20)),
                ('img', models.URLField()),
                ('context', models.TextField()),
            ],
            options={
                'db_table': 'nba_news',
            },
        ),
    ]
