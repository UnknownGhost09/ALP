# Generated by Django 4.1.4 on 2023-09-05 09:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_membership_plan_id_alter_businesslogs_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="businesslogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 884508), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="businesslogs",
            name="plan_id",
            field=models.ForeignKey(
                db_column="plan_id",
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.membership",
            ),
        ),
        migrations.AlterField(
            model_name="changesponserlogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 884508), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="farmingroilogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 885508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="levelincome",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 887508), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="newsmodel",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 886508), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="ptransfer",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 889508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="stakingroilogs",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 886508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="status_activity",
            name="time",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 888509), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="ticketmodel",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 888509), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 882508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 882508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="usercofounderclub",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 890508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="usermembership",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 885508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userrank",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 890508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userreferral",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 889508), max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="userstaking",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 885508), max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userwithdrawls",
            name="date",
            field=models.CharField(
                default=datetime.datetime(2023, 9, 5, 9, 18, 37, 888509), max_length=200
            ),
        ),
    ]
