# Generated by Django 3.0.1 on 2022-04-20 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userReport', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='agegroup',
            table='age_group',
        ),
        migrations.AlterModelTable(
            name='gender',
            table='gender',
        ),
        migrations.AlterModelTable(
            name='initialreport',
            table='initial_report',
        ),
        migrations.AlterModelTable(
            name='region',
            table='region',
        ),
        migrations.AlterModelTable(
            name='reportdatamining',
            table='report_data_minining',
        ),
        migrations.AlterModelTable(
            name='reporttype',
            table='report_type',
        ),
        migrations.AlterModelTable(
            name='userreport',
            table='user_report',
        ),
    ]
