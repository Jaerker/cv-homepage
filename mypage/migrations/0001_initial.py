# Generated by Django 3.0.3 on 2020-02-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_name', models.CharField(max_length=40)),
                ('achievement_description', models.TextField()),
            ],
        ),
    ]
