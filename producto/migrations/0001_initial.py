# Generated by Django 5.0.3 on 2024-03-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
    ]
