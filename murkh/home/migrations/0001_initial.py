# Generated by Django 4.0.2 on 2022-07-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('overview', models.CharField(max_length=1000)),
                ('rating', models.FloatField()),
                ('release', models.DateField()),
            ],
        ),
    ]
