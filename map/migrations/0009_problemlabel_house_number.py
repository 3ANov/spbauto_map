# Generated by Django 3.0.3 on 2020-03-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_problemlabel_state_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemlabel',
            name='house_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='номер дома'),
        ),
    ]
