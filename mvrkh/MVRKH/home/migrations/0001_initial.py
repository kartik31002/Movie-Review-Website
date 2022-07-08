# Generated by Django 4.0.6 on 2022-07-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('movieid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('overview', models.TextField()),
                ('rating', models.CharField(max_length=10)),
                ('release', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('review', models.TextField()),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movies')),
            ],
        ),
    ]
