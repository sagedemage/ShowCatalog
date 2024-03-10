# Generated by Django 5.0.2 on 2024-02-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('age_rating', models.CharField(max_length=255)),
            ],
        ),
    ]
