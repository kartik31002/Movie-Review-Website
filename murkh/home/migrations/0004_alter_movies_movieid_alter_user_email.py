# Generated by Django 4.0.6 on 2022-07-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_reviews_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movieid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
