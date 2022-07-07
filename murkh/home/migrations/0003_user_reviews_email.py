# Generated by Django 4.0.6 on 2022-07-07 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_movies_id_alter_movies_movieid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(default='abcd@example.com', max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='email',
            field=models.ForeignKey(default='abcd@example.com', on_delete=django.db.models.deletion.CASCADE, to='home.user'),
            preserve_default=False,
        ),
    ]
