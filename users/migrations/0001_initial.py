# Generated by Django 2.1.3 on 2018-11-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('place_of_live', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('about_be', models.TextField()),
                ('age', models.IntegerField()),
                ('favorite_genres', models.CharField(max_length=50)),
                ('favorite_writers', models.CharField(max_length=50)),
            ],
        ),
    ]
