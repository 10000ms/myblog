# Generated by Django 2.2 on 2019-05-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_daterecord_read_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='city_id',
            field=models.IntegerField(default=0, verbose_name='city_id'),
        ),
        migrations.AddField(
            model_name='region',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='纬度值'),
        ),
        migrations.AddField(
            model_name='region',
            name='lng',
            field=models.FloatField(default=0.0, verbose_name='经度值'),
        ),
        migrations.AlterField(
            model_name='region',
            name='city',
            field=models.CharField(max_length=20, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='region',
            name='province',
            field=models.CharField(max_length=10, verbose_name='省份'),
        ),
    ]
