# Generated by Django 3.1.3 on 2020-11-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'MySubscriber',
                'verbose_name_plural': 'A lot of Subscribers',
            },
        ),
    ]
