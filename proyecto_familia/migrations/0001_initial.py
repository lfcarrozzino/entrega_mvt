# Generated by Django 4.0.3 on 2022-04-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_cumpleaños', models.DateField()),
                ('parentesco', models.CharField(max_length=40)),
            ],
        ),
    ]
