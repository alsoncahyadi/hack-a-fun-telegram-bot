# Generated by Django 2.1.4 on 2019-02-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0002_auto_20190211_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='salt',
            field=models.CharField(max_length=16, verbose_name="Player's salt"),
        ),
    ]
