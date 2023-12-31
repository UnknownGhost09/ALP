# Generated by Django 4.1.4 on 2023-09-04 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="businesslogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 569148), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="changesponserlogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 570080), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="farmingroilogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 571084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="levelincome",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 572084), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="newsmodel",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 571084), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="ptransfer",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 574084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="stakingroilogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 571084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="status_activity",
            name="time",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 574084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="ticketmodel",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 573085), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 566016), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 566016), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="usercofounderclub",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 575084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="usermembership",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 570080), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userrank",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 576084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userreferral",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 574084), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="userstaking",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 571084), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userwithdrawls",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 4, 6, 7, 44, 573085), max_length=200
            ),
        ),
    ]
