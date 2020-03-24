# Generated by Django 3.0.3 on 2020-03-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_statedistrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemlabel',
            name='state_district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.StateDistrict', verbose_name='район города'),
        ),
    ]
